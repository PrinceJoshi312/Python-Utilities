# QuickMail: Automated Result Delivery System

A modular Python-based email automation tool designed to send personalized HTML reports from Excel/CSV data.

## 🚀 Features

- **Batch Processing:** Sends hundreds of emails in a single SMTP session.
- **HTML Templating:** Supports external `.html` templates with dynamic placeholders.
- **Excel/CSV Support:** Load recipient data directly from spreadsheets.
- **Secure Credentials:** Uses environment variables (`.env`) to protect your email password.
- **Context Management:** Automatically handles SMTP connection opening and closing.

## 📁 Project Structure

```text
std_email_automation/
├── mailer/              # Core Package (Reusable)
│   ├── core.py          # SMTP engine
│   └── utils.py         # Data & template loaders
├── templates/           # Email HTML/Text designs
├── .env.template        # Sample configuration
├── main.py              # Main execution script
├── students.xlsx        # Your data source
└── requirements.txt     # Dependencies
```

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.8+
- A Gmail account with **2-Step Verification** enabled.
- A **Gmail App Password** (16-character code). [How to get one](https://support.google.com/accounts/answer/185833).

### 2. Installation
Clone or download this folder, then install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
1. Rename `.env.template` to `.env`.
2. Open `.env` and enter your credentials:
   ```text
   SENDER_EMAIL=your-email@gmail.com
   SENDER_PASSWORD=abcd-efgh-ijkl-mnop
   ```

### 4. Data Setup
Ensure your `students.xlsx` has at least an `Email` column and a `Name` column. Any other columns (like `Maths`, `Physics`) can be used in your templates as `{maths}`, `{physics}`, etc.

## 📧 Usage

1. Edit your HTML design in `templates/report.html`.
2. Run the automation:
   ```bash
   python main.py
   ```

## 💡 How it Works

The script uses a custom `QuickMail` class that acts as a **Context Manager**. It logs in once, iterates through your spreadsheet, fills your HTML template with each student's specific grades, and sends the emails with a slight delay to avoid spam filters.

---
*Created with Gemini CLI*
