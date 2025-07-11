import streamlit as st
import json # Required for displaying JSON nicely
from llm_handler import analyze_vulnerability_with_llm # Import the analysis function

# --- Streamlit Page Configuration ---
# Sets the title in the browser tab and the layout. 'wide' uses more screen space.
st.set_page_config(page_title="LLM-Powered Vulnerability Advisor", layout="wide")
# --- Header and Introduction ---
st.title("🛡️ LLM-Powered Vulnerability Advisor")
st.markdown(
    """
    This tool leverages Large Language Models (LLMs) to intelligently analyze raw vulnerability reports,
    extract key details, assess potential impact, and provide actionable recommendations for security teams.
    Simply paste a vulnerability description below and let the AI do the heavy lifting!
    """
)

# --- Input Area ---
# Text area for the user to paste the vulnerability report
vulnerability_input = st.text_area(
    "Paste Raw Vulnerability Report Here:",
    height=300, # Adjust height as needed
    placeholder="e.g., CVE description, vendor advisory, security blog post...",
    key="vulnerability_input_text" # Unique key for this widget
)

# Button to trigger the analysis
process_button = st.button("Analyze Vulnerability", key="analyze_vulnerability_button")

# --- Conditional Logic for Analysis ---
# This block executes when the button is clicked AND there's input text
if process_button and vulnerability_input:
    with st.spinner("Analyzing with LLM... This may take a moment."):
        # Call the LLM analysis function from llm_handler.py
        analysis_result = analyze_vulnerability_with_llm(vulnerability_input)

        # Check if an error occurred during analysis
        if "error" in analysis_result:
            st.error(f"Error during analysis: {analysis_result.get('details', 'An unknown error occurred. Check console.')}")
            # Optionally display raw error for debugging
            st.subheader("Raw Error Details (for debugging):")
            st.json(analysis_result)
        else:
            st.success("Analysis Complete!")
            st.write("---") # Separator

            # --- Display Structured Output ---
            st.subheader("📊 Vulnerability Analysis Summary")

            # Extract top-level keys for cleaner display
            vulnerability_details = analysis_result.get("Vulnerability_Analysis", {})
            potential_impact = analysis_result.get("Potential_Impact", "N/A")
            actionable_recommendation = analysis_result.get("Actionable_Recommendation", {})

            # Use Streamlit columns for a nicer layout
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### Key Details")
                # Displaying as JSON initially for quick setup, but you can format this more
                st.json(vulnerability_details)
                # Example of more formatted display (uncomment and replace st.json above if preferred)
                # st.write(f"**Vulnerability ID:** {vulnerability_details.get('Vulnerability_ID', 'N/A')}")
                # st.write(f"**Vulnerable Products:** {', '.join(vulnerability_details.get('Vulnerable_Products', ['N/A']))}")
                # st.write(f"**Severity:** {vulnerability_details.get('Severity', 'N/A')}")
                # st.write(f"**Type:** {vulnerability_details.get('Vulnerability_Type', 'N/A')}")
                # st.write(f"**Description:** {vulnerability_details.get('Brief_Description', 'N/A')}")
                # st.write(f"**Exploit Status:** {vulnerability_details.get('Exploit_Status', 'N/A')}")
                # st.markdown(f"**References:**")
                # for ref in vulnerability_details.get('References', []):
                #     st.markdown(f"- {ref}")

            with col2:
                st.markdown("#### Actionable Recommendation")
                # Displaying as JSON initially, can be formatted more
                st.json(actionable_recommendation)
                # Example of more formatted display (uncomment and replace st.json above if preferred)
                # st.write(f"**Primary Mitigation:** {actionable_recommendation.get('Primary_Mitigation', 'N/A')}")
                # st.write(f"**Urgency Level:** {actionable_recommendation.get('Urgency_Level', 'N/A')}")
                # st.markdown(f"**Secondary Mitigations/Workarounds:**")
                # for item in actionable_recommendation.get('Secondary_Mitigations_Workarounds', ['N/A']):
                #     st.markdown(f"- {item}")
                # st.markdown(f"**Verification Steps:**")
                # for item in actionable_recommendation.get('Verification_Steps', ['N/A']):
                #     st.markdown(f"- {item}")

            st.markdown("#### Potential Impact")
            st.info(potential_impact) # st.info displays text in a blue box

            # Optional: Expandable section to show the raw JSON from LLM (useful for debugging)
            with st.expander("Show Raw LLM Output (for debugging)"):
                st.json(analysis_result)

# Message if button is clicked but input is empty
elif process_button and not vulnerability_input:
    st.warning("Please paste a vulnerability report to analyze.")

# Instructions when the app first loads or after an analysis
st.markdown("---")
st.markdown("### How to Use:")
st.markdown("1. Copy a raw vulnerability description (e.g., from a CVE, security advisory, or news article).")
st.markdown("2. Paste it into the text area above.")
st.markdown("3. Click 'Analyze Vulnerability' to get a structured summary and recommendations.")