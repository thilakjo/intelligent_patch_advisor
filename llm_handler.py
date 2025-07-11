import os
import google.generativeai as genai
from dotenv import load_dotenv
import json  # Ensure json is imported for parsing the LLM response
# Load environment variables from .env file
# This line should be at the very top of your script to ensure env vars are loaded first
load_dotenv()

# --- Configuration ---
# Retrieve the Gemini API key from environment variables
# Make sure you have GEMINI_API_KEY set in your .env file
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    # It's good practice to provide a clear error message if the key isn't found
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in a .env file located at your project root.")

# Configure the Google Gemini API
genai.configure(api_key=API_KEY)

# Initialize the Generative Model
# Directly specify 'gemini-1.5-flash' as recommended by the error message.
# If this model is not available for your API key/region, this will raise an error.
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    print(f"Using directly specified model: {model.model_name}") # For debugging
except Exception as e:
    # If gemini-1.5-flash fails, try gemini-1.5-pro as a backup
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        print(f"Using directly specified model: {model.model_name}") # For debugging
    except Exception as e_pro:
        # If both 1.5 models fail, raise an error
        raise RuntimeError(f"Failed to initialize generative models. 'gemini-1.5-flash' and 'gemini-1.5-pro' might not be available for your API key or region. Original error: {e_pro}")
    
# --- Prompt Engineering ---
VULNERABILITY_ANALYSIS_PROMPT_TEMPLATE = """
You are an expert cybersecurity analyst with extensive knowledge of vulnerability management and patch processes.
Your task is to analyze the provided raw vulnerability report.
From this report, you must extract all critical information, assess its potential impact, and provide a clear, actionable recommendation for a security operations team.

**Strictly adhere to the following steps and output format:**

1.  **Extract Key Details**: Identify the following. If a detail is not explicitly provided in the *given raw report*, state "Not provided" or "N/A" for lists:
    * **Vulnerability_ID**: The official ID (e.g., CVE-YYYY-XXXXX, Vendor-Specific-ID, or internal tracking ID).
    * **Vulnerable_Products**: A list of affected software/hardware, including specific versions or version ranges if mentioned.
    * **Severity**: Rate as Critical, High, Medium, or Low. Provide a brief justification based solely on the report's content.
    * **Vulnerability_Type**: Briefly describe the class of vulnerability (e.g., Remote Code Execution (RCE), SQL Injection, Cross-Site Scripting (XSS), Denial of Service (DoS), Privilege Escalation, Information Disclosure, Buffer Overflow).
    * **Brief_Description**: A concise, technical summary (1-3 sentences) of what the vulnerability is and how it functions.
    * **Exploit_Status**: Is it actively exploited in the wild, publicly disclosed (Proof-of-Concept available), theoretical, or unknown based on the report?
    * **References**: A list of relevant links to official advisories, patches, security blogs, or NVD entries.

2.  **Assess Potential Impact**:
    * Describe the worst-case scenario if this vulnerability is successfully exploited.
    * Consider potential consequences like data compromise (confidentiality, integrity, availability), financial loss, or reputational damage.
    * This should be a concise paragraph (2-4 sentences).

3.  **Provide Actionable Recommendation**:
    * **Primary_Mitigation**: The most direct and important action to take (e.g., "Apply vendor patch KBXXXXXX", "Upgrade to version A.B.C", "Implement specific configuration change").
    * **Secondary_Mitigations_Workarounds**: A list of additional protective measures or temporary fixes if the primary mitigation is not immediately possible (e.g., "Block port YYYY at firewall", "Disable feature Z", "Implement IPS/IDS rule"). State "N/A" if none are mentioned or obvious.
    * **Urgency_Level**: Assign a practical urgency: "Immediate" (within hours/day), "High Priority" (within 1-3 days), "Medium Priority" (within 1 week), or "Low Priority" (plan for next patch cycle). Justify briefly based on severity, exploit status, and potential impact.
    * **Verification_Steps**: A list of steps the team can take to confirm the mitigation was successful (e.g., "Run vulnerability scan with Tool A", "Check product version to confirm upgrade", "Monitor logs for abnormal activity"). State "N/A" if none are mentioned or obvious.

4.  **Format the entire output as a single, valid JSON object.**
    * Ensure all keys are enclosed in double quotes.
    * Lists must be JSON arrays (`[]`).
    * Do not include any introductory or concluding text, or markdown code block delimiters (```json) outside the JSON object itself.

---
**RAW VULNERABILITY REPORT:**
{vulnerability_text}
---

**STRICTLY ADHERE TO THIS JSON OUTPUT FORMAT:**
```json
{{
    "Vulnerability_Analysis": {{
        "Vulnerability_ID": "CVE-YYYY-XXXXX",
        "Vulnerable_Products": [
            "Product Name (Versions < X.Y.Z)",
            "Another Product (Versions A.B.C - D.E.F)"
        ],
        "Severity": "Critical",
        "Vulnerability_Type": "Remote Code Execution",
        "Brief_Description": "A concise technical summary of the vulnerability.",
        "Exploit_Status": "Actively exploited in the wild",
        "References": [
            "https://official.vendor.com/advisory/CVE-YYYY-XXXXX",
            "https://nvd.nist.gov/vuln/detail/CVE-YYYY-XXXXX"
        ]
    }},
    "Potential_Impact": "A detailed description of the worst-case scenario upon exploitation.",
    "Actionable_Recommendation": {{
        "Primary_Mitigation": "Apply vendor-provided patch KBXXXXXX. Upgrade affected systems to the latest secure version.",
        "Secondary_Mitigations_Workarounds": [
            "Implement IPS/IDS signatures.",
            "Restrict network access to vulnerable services."
        ],
        "Urgency_Level": "Immediate",
        "Verification_Steps": [
            "Conduct authenticated vulnerability scans.",
            "Verify product version numbers."
        ]
    }}
}}
```"""

def analyze_vulnerability_with_llm(vulnerability_text: str) -> dict:
    """
    Sends the vulnerability text to the LLM for analysis and returns structured information.

    Args:
        vulnerability_text (str): The raw text of the vulnerability report.

    Returns:
        dict: A dictionary containing the parsed vulnerability analysis and recommendations.
              Returns an error dictionary if analysis or parsing fails.
    """
    if not vulnerability_text.strip():
        return {"error": "Input vulnerability text cannot be empty."}

    try:
        # Construct the prompt with the actual vulnerability text
        full_prompt = VULNERABILITY_ANALYSIS_PROMPT_TEMPLATE.format(
            vulnerability_text=vulnerability_text
        )

        # Generate content using the LLM
        response = model.generate_content(full_prompt)

        # Access the text from the response object
        response_text = response.text.strip()

        # Attempt to clean the response if it includes markdown code blocks
        if response_text.startswith("```json") and response_text.endswith("```"):
            response_text = response_text[len("```json"):-len("```")].strip()
        elif response_text.startswith("```") and response_text.endswith("```"):
            response_text = response_text[len("```"):-len("```")].strip()

        # Parse the JSON string into a Python dictionary
        parsed_response = json.loads(response_text)
        return parsed_response

    except json.JSONDecodeError as e:
        print(f"JSON Decoding Error: Failed to parse LLM response as valid JSON: {e}")
        print(f"Raw LLM response was: \n---\n{response_text if 'response_text' in locals() else 'No response text available'}\n---")
        return {"error": "Failed to parse LLM response as JSON. The LLM might have hallucinated or not adhered to the format.", "details": str(e), "llm_raw_response": response_text if 'response_text' in locals() else 'N/A'}
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return {"error": "Configuration error: " + str(e)}
    except Exception as e:
        print(f"An unexpected error occurred during LLM analysis: {e}")
        return {"error": "An unexpected error occurred during LLM analysis.", "details": str(e)}

if __name__ == "__main__":
    # Example Usage for testing this file directly
    print("--- Testing llm_handler.py directly with a dummy vulnerability ---")

    dummy_vulnerability_text = """
    Title: Apache Log4j2 Remote Code Execution (CVE-2021-44228) - "Log4Shell"
    A critical remote code execution (RCE) vulnerability, identified as CVE-2021-44228 and commonly known as "Log4Shell", has been discovered in Apache Log4j2 versions 2.0-beta9 to 2.14.1. This flaw allows an unauthenticated attacker to execute arbitrary code on a remote server by logging a specially crafted string. This vulnerability is extremely severe due to Log4j2's widespread use in enterprise Java applications and services. Active exploitation has been widely observed in the wild.

    Mitigation:
    1.  Upgrade Log4j2 to version 2.17.1 or later (Java 8 and later).
    2.  For previous versions (2.10 to 2.14.1), set the system property `log4j2.formatMsgNoLookups` to `true` or remove the `JndiLookup` class from the classpath (e.g., `zip -q -d log4j-core-*.jar org/apache/logging/log4j/core/lookup/JndiLookup.class`).
    3.  Implement network-level blocking of outbound LDAP/RMI connections from vulnerable systems.

    References:
    - Apache Log4j Security Vulnerabilities: https://logging.apache.org/log4j/2.x/security.html
    - CISA Advisory: https://www.cisa.gov/uscert/apache-log4j-vulnerability-guidance
    - NVD: https://nvd.nist.gov/vuln/detail/CVE-2021-44228
    """

    analysis_result = analyze_vulnerability_with_llm(dummy_vulnerability_text)
    print("\n--- LLM Analysis Result ---")
    print(json.dumps(analysis_result, indent=4))
    print("\n---------------------------\n")

    # Test with empty input
    print("\n--- Testing with empty input ---")
    empty_result = analyze_vulnerability_with_llm("")
    print(json.dumps(empty_result, indent=4))
