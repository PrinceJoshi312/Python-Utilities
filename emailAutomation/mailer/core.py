import smtplib
import time
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from typing import List, Optional, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuickMail:
    """A context-managed SMTP mailer for bulk and single emails."""

    def __init__(self, smtp_server="smtp.gmail.com", port=587, use_tls=True):
        self.server_addr = smtp_server
        self.port = port
        self.use_tls = use_tls
        self.server = None
        self.is_logged_in = False
        self._sender_email = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def login(self, email: str, password: str):
        """Log in to the SMTP server."""
        try:
            self.server = smtplib.SMTP(self.server_addr, self.port)
            if self.use_tls:
                self.server.starttls()
            self.server.login(email, password)
            self._sender_email = email
            self.is_logged_in = True
            logging.info(f"Successfully logged in as {email}")
        except Exception as e:
            logging.error(f"Login failed: {e}")
            raise

    def send(self, to: str, subject: str, body: str, html_body: Optional[str] = None, attachments: Optional[List[str]] = None):
        """
        Send a single email. 
        If html_body is provided, it sends a multipart/alternative email with both plain and HTML versions.
        """
        if not self.is_logged_in:
            raise Exception("You must call .login() before sending.")

        msg = MIMEMultipart("mixed")
        msg["From"] = self._sender_email
        msg["To"] = to
        msg["Subject"] = subject

        # Create the body part (alternative: plain vs html)
        body_part = MIMEMultipart("alternative")
        body_part.attach(MIMEText(body, "plain"))
        if html_body:
            body_part.attach(MIMEText(html_body, "html"))
        
        msg.attach(body_part)

        # Attach files
        if attachments:
            for file_path in attachments:
                try:
                    with open(file_path, "rb") as f:
                        part = MIMEApplication(f.read(), Name=file_path.split("/")[-1])
                    part['Content-Disposition'] = f'attachment; filename="{file_path.split("/")[-1]}"'
                    msg.attach(part)
                except Exception as e:
                    logging.warning(f"Failed to attach {file_path}: {e}")

        try:
            self.server.send_message(msg)
            logging.info(f"Email sent to {to}")
        except Exception as e:
            logging.error(f"Failed to send email to {to}: {e}")

    def batch_send(self, recipients: List[Dict[str, Any]], template: str, subject: str, is_html: bool = False, delay: float = 1.0):
        """
        Send emails to a list of recipients.
        If is_html is True, the template is treated as HTML.
        """
        for count, data in enumerate(recipients, 1):
            try:
                content = template.format(**data)
                
                if is_html:
                    # For HTML emails, it's good practice to provide a plain text fallback
                    # Here we just strip tags for a simple fallback or use a generic message
                    plain_fallback = f"Please view this email in an HTML-compatible client."
                    self.send(data['email'], subject, plain_fallback, html_body=content)
                else:
                    self.send(data['email'], subject, content)
                
                if delay > 0 and count < len(recipients):
                    time.sleep(delay)
            except Exception as e:
                logging.error(f"Batch error for {data.get('email', 'unknown')}: {e}")

    def quit(self):
        """Close the connection."""
        if self.server:
            try:
                self.server.quit()
                logging.info("SMTP connection closed.")
            except:
                pass
            finally:
                self.server = None
                self.is_logged_in = False
