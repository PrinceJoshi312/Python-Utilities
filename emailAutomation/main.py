import os
from dotenv import load_dotenv
from mailer import QuickMail, load_from_excel, load_template

# Load environment variables
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

def main():
    # 1. Load recipient data
    recipients = load_from_excel("students.xlsx")
    if not recipients:
        return

    # 2. Load the external HTML template
    template_content = load_template("templates/report.html")
    if not template_content:
        print("Error: Could not load template file.")
        return

    # 3. Validation
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("Error: Check your .env file for credentials.")
        return

    # 4. Process Mailing
    with QuickMail() as mailer:
        try:
            mailer.login(SENDER_EMAIL, SENDER_PASSWORD)
            
            print(f"Sending {len(recipients)} reports using external template...")
            mailer.batch_send(
                recipients=recipients, 
                template=template_content, 
                subject="Your Academic Progress Report",
                is_html=True
            )
            print("Batch processing complete.")

        except Exception as e:
            print(f"Critical Error: {e}")

if __name__ == "__main__":
    main()
