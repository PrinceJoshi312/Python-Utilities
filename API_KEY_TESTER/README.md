# Gemini API Test Setup

This project helps you test the Google Gemini API using the new `google-genai` Python SDK.

## Setup Instructions

1.  **Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    ```

2.  **Activate the Virtual Environment:**
    -   Windows: `.venv\Scripts\activate`
    -   Mac/Linux: `source .venv/bin/activate`

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key:**
    -   Copy `.env.template` to `.env`.
    -   Get your API key from [Google AI Studio](https://aistudio.google.com/).
    -   Paste your key into the `.env` file.

5.  **Run the Test:**
    ```bash
    python test_gemini.py
    ```
