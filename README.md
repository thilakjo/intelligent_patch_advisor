# 🛡️ Intelligent Patch Advisor

**LLM-Powered Vulnerability Analysis**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/) [![Streamlit](https://img.shields.io/badge/streamlit-%E2%89%A50.85-orange)](https://streamlit.io/)

---

## 📖 Table of Contents

1. [Project Overview](#project-overview)
2. [✨ Features](#-features)
3. [🎬 Demo Screenshots](#-demo-screenshots)
4. [🚀 Quickstart](#-quickstart)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Configuration](#configuration)
   - [Running the App](#running-the-app)
5. [🗂️ Project Structure](#️-project-structure)
6. [👨‍💻 Team](#-team)
7. [📄 License](#-license)

---

## Project Overview

`Intelligent Patch Advisor` is an AI-driven tool that automates vulnerability triage by converting raw security advisories into structured, actionable insights. It leverages Google Gemini LLMs to extract:

- **Key Details**: CVE ID, affected products, severity, vulnerability type, exploit status.
- **Impact Assessment**: Potential worst-case scenarios.
- **Recommendations**: Prioritized mitigation steps, urgency levels, and validation procedures.

This solution accelerates patch planning, reduces manual overhead, and helps security teams respond faster to emerging threats.

---

## ✨ Features

- **LLM-Powered Analysis**: Deep parsing of unstructured reports using Google Gemini.
- **Structured JSON Output**: Consistent, easy-to-parse format for integrations.
- **Actionable Guidance**: Clear primary and secondary mitigation actions with verification steps.
- **Web UI**: Streamlit-based interface for quick vulnerability lookups.
- **Local Execution**: No cloud dependency; run entirely on your machine.

---

## 🎬 Demo Screenshots

<p align="center">
  <img src="screenshots/Screenshot%202025-07-11%20at%2010.04.56%E2%80%AFPM.png" alt="App Input/Output" width="45%" />
  <img src="screenshots/Screenshot%202025-07-11%20at%2010.05.48%E2%80%AFPM.png" alt="Analysis Result" width="45%" />
</p>

---

## 🚀 Quickstart

### Prerequisites

- Python 3.8+ installed
- A Google Gemini API Key (obtain from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Installation

```bash
# Clone the repository
git clone https://github.com/thilakjo/intelligent_patch_advisor.git
cd intelligent_patch_advisor

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate.bat  # Windows CMD
# venv\Scripts\Activate.ps1  # Windows PowerShell

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file in the project root:
   ```ini
   GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
   ```
2. Replace the placeholder with your Google Gemini key.

### Running the App

```bash
streamlit run main.py
```

Open your browser at `http://localhost:8501`, paste a vulnerability report, and click **Analyze Vulnerability**.

---

## 🗂️ Project Structure

```bash
.
├── _pycache__/              # Compiled Python files
├── docs/                    # Additional documentation
│   ├── documentation.md
│   └── Intelligent Patch Advisor.pdf
├── llm_handler.py           # LLM integration and prompt logic
├── main.py                  # Streamlit application entrypoint
├── presentation/            # Hackathon slide deck
│   └── Thilak - jo team.pdf
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── sample_vulnerabilities/  # Test CVE and advisory samples
│   ├── cve_example_1.txt
│   ├── cve_example_2.txt
│   └── vendor_advisory_sample.txt
├── screenshots/             # UI screenshots
│   ├── Screenshot 2025-07-11 at 10.04.56 PM.png
│   └── Screenshot 2025-07-11 at 10.05.48 PM.png
└── video/                   # Demo recording
```

---

## 👨‍💻 Team

- **Jo-Team**: Thilak S (RVCE - 1RV22EC171)  
  Portfolio: https://thilakjo.com

---
