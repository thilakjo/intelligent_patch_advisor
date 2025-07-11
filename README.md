# 🛡️ Intelligent Patch Advisor - LLM-Powered Vulnerability Analysis

## Project Overview

The "Intelligent Patch Advisor" is an AI-powered tool designed to streamline the critical process of vulnerability management. In today's fast-paced cybersecurity landscape, security teams are often overwhelmed by a deluge of raw vulnerability reports from various sources (CVEs, vendor advisories, security blogs). Manually sifting through these, extracting key details, assessing impact, and formulating actionable remediation plans is time-consuming, prone to error, and delays critical patching.

This tool leverages advanced Large Language Models (LLMs) to automatically ingest raw vulnerability text and transform it into structured, actionable insights, providing immediate clarity on:

- Key vulnerability details (ID, affected products, severity, type, description, exploit status).
- Potential worst-case impacts.
- Clear, prioritized, and actionable recommendations for primary and secondary mitigations, urgency levels, and verification steps.

Our goal is to significantly reduce the manual effort and time required for vulnerability triage, enabling security operations teams to respond faster and more effectively to emerging threats.

## ✨ Features

- **LLM-Powered Analysis**: Utilizes state-of-the-art Google Gemini models for deep understanding of vulnerability reports.
- **Structured Output**: Transforms unstructured text into a consistent, easy-to-read JSON-like format.
- **Actionable Recommendations**: Provides immediate and clear guidance on how to mitigate vulnerabilities, including urgency and verification steps.
- **User-Friendly Interface**: Built with Streamlit for an intuitive web-based experience.
- **Local Execution**: Easily runnable on your local machine with minimal setup.

## 🚀 How to Run

Follow these steps to set up and run the Intelligent Patch Advisor on your local machine.

### Prerequisites

- Python 3.8+ installed
- A Google Gemini API Key (obtainable from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Setup Steps

1.  **Clone the Repository (if applicable, otherwise navigate to your project folder):**

    ```bash
    # If you're starting from a fresh clone
    git clone <your-repo-link>
    cd intelligent_patch_advisor
    ```

    (If you've been following my instructions, you are likely already in the `intelligent_patch_advisor` directory.)

2.  **Create a Python Virtual Environment:**
    It's best practice to use a virtual environment to manage project dependencies.

    ```bash
    python3 -m venv venv
    ```

3.  **Activate the Virtual Environment:**

        - **macOS / Linux:**
          ```bash
          source venv/bin/activate
          ```
        - **Windows (Command Prompt):**
          ```bash
          venv\Scripts\activate.bat
          ```
        - **Windows (PowerShell):**
          `bash

    venv\Scripts\Activate.ps1
    `      (You should see`(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.)

4.  **Install Dependencies:**
    All required libraries are listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Up Your Google Gemini API Key:**

    - Create a file named `.env` in the root directory of your project (the same directory as `main.py` and `llm_handler.py`).
    - Open the `.env` file and add your Gemini API key in the following format. **Replace `YOUR_ACTUAL_GEMINI_API_KEY_HERE` with your real key.**
      ```
      GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
      ```
      _Example:_ `GEMINI_API_KEY="AIzaSy...your_actual_key_here...sM"`

6.  **Run the Streamlit Application:**
    Ensure your virtual environment is still active, then run:
    ```bash
    streamlit run main.py
    ```
    Your default web browser should automatically open the application at `http://localhost:8501`.

## ✍️ How to Use

1.  **Open the Application**: After running `streamlit run main.py`, the web interface will appear in your browser.
2.  **Paste Vulnerability Report**: Copy the raw text of a vulnerability report (e.g., from a CVE description, a vendor security advisory, or a security news article).
3.  **Analyze**: Paste the copied text into the large text area provided in the application.
4.  **Get Insights**: Click the "Analyze Vulnerability" button. The LLM will process the text and display a structured summary, including key details, potential impact, and actionable recommendations.

## 📁 Project Structure

Excellent! Confirming that all sample vulnerabilities work correctly is a great step. That means your core application and LLM integration are solid.

Now, let's move onto generating the content for your documentation and presentation files. We'll start with the most important one for most hackathons: the README.md.

9. README.md
   The README.md file is crucial. It's the first thing judges and other developers will look at to understand your project, how to run it, and what it does.

File Path: your_hackathon_project/README.md

Content: Copy and paste the entire block below into your README.md file, replacing any existing content. Make sure to fill in your actual API Key instructions and your Team Members section.

Markdown

# 🛡️ Intelligent Patch Advisor - LLM-Powered Vulnerability Analysis

## Project Overview

The "Intelligent Patch Advisor" is an AI-powered tool designed to streamline the critical process of vulnerability management. In today's fast-paced cybersecurity landscape, security teams are often overwhelmed by a deluge of raw vulnerability reports from various sources (CVEs, vendor advisories, security blogs). Manually sifting through these, extracting key details, assessing impact, and formulating actionable remediation plans is time-consuming, prone to error, and delays critical patching.

This tool leverages advanced Large Language Models (LLMs) to automatically ingest raw vulnerability text and transform it into structured, actionable insights, providing immediate clarity on:

- Key vulnerability details (ID, affected products, severity, type, description, exploit status).
- Potential worst-case impacts.
- Clear, prioritized, and actionable recommendations for primary and secondary mitigations, urgency levels, and verification steps.

Our goal is to significantly reduce the manual effort and time required for vulnerability triage, enabling security operations teams to respond faster and more effectively to emerging threats.

## ✨ Features

- **LLM-Powered Analysis**: Utilizes state-of-the-art Google Gemini models for deep understanding of vulnerability reports.
- **Structured Output**: Transforms unstructured text into a consistent, easy-to-read JSON-like format.
- **Actionable Recommendations**: Provides immediate and clear guidance on how to mitigate vulnerabilities, including urgency and verification steps.
- **User-Friendly Interface**: Built with Streamlit for an intuitive web-based experience.
- **Local Execution**: Easily runnable on your local machine with minimal setup.

## 🚀 How to Run

Follow these steps to set up and run the Intelligent Patch Advisor on your local machine.

### Prerequisites

- Python 3.8+ installed
- A Google Gemini API Key (obtainable from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Setup Steps

1.  **Clone the Repository (if applicable, otherwise navigate to your project folder):**

    ```bash
    # If you're starting from a fresh clone
    git clone <your-repo-link>
    cd intelligent_patch_advisor
    ```

    (If you've been following my instructions, you are likely already in the `intelligent_patch_advisor` directory.)

2.  **Create a Python Virtual Environment:**
    It's best practice to use a virtual environment to manage project dependencies.

    ```bash
    python3 -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    - **macOS / Linux:**
      ```bash
      source venv/bin/activate
      ```
    - **Windows (Command Prompt):**
      ```bash
      venv\Scripts\activate.bat
      ```
    - **Windows (PowerShell):**
      `bash
venv\Scripts\Activate.ps1
`
      (You should see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.)

4.  **Install Dependencies:**
    All required libraries are listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Up Your Google Gemini API Key:**

    - Create a file named `.env` in the root directory of your project (the same directory as `main.py` and `llm_handler.py`).
    - Open the `.env` file and add your Gemini API key in the following format. **Replace `YOUR_ACTUAL_GEMINI_API_KEY_HERE` with your real key.**
      ```
      GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
      ```
      _Example:_ `GEMINI_API_KEY="AIzaSy...your_actual_key_here...sM"`

6.  **Run the Streamlit Application:**
    Ensure your virtual environment is still active, then run:
    ```bash
    streamlit run main.py
    ```
    Your default web browser should automatically open the application at `http://localhost:8501`.

## ✍️ How to Use

1.  **Open the Application**: After running `streamlit run main.py`, the web interface will appear in your browser.
2.  **Paste Vulnerability Report**: Copy the raw text of a vulnerability report (e.g., from a CVE description, a vendor security advisory, or a security news article).
3.  **Analyze**: Paste the copied text into the large text area provided in the application.
4.  **Get Insights**: Click the "Analyze Vulnerability" button. The LLM will process the text and display a structured summary, including key details, potential impact, and actionable recommendations.

## 📁 Project Structure

intelligent_patch_advisor/
├── .env # Your Google Gemini API Key (create this file!)
├── .gitignore # Specifies intentionally untracked files to ignore
├── requirements.txt # Python dependencies
├── main.py # The Streamlit web application interface
├── llm_handler.py # Contains the LLM integration logic and prompt engineering
├── README.md # This file!
├── docs/ # Documentation files (e.g., detailed technical docs)
│ └── documentation.md # Detailed project documentation (to be filled)
├── presentation/ # Presentation slides for the hackathon
│ └── presentation_slides.pptx # (Example, use your preferred format)
├── sample_vulnerabilities/ # Sample vulnerability reports for testing/demo
│ ├── cve_example_1.txt
│ ├── cve_example_2.txt
│ └── vendor_advisory_sample.txt
└── venv/ # Python virtual environment (ignored by Git)

## 👨‍💻 Team Members

- **Jo-team**
- Thilak S - RVCE - 1RV22EC171

---
