import os
import smtplib
import json
import urllib.error
import urllib.request
from email.message import EmailMessage


class EmailService:
    def __init__(self):
        self.sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
        self.sendgrid_from_email = os.getenv("SENDGRID_FROM_EMAIL")
        self.host = os.getenv("SMTP_HOST")
        self.port = int(os.getenv("SMTP_PORT", "587"))
        self.username = os.getenv("SMTP_USERNAME")
        self.password = os.getenv("SMTP_PASSWORD")
        self.sender = os.getenv("SMTP_FROM", self.username or "")

    def send_email(self, to: str, subject: str, body: str):
        if not to:
            return False, "Δεν υπάρχει email παραλήπτη."

        if self.sendgrid_api_key:
            return self.send_email_with_sendgrid(to, subject, body)

        return self.send_email_with_smtp(to, subject, body)

    def send_email_with_sendgrid(self, to: str, subject: str, body: str):
        if not self.sendgrid_from_email:
            return False, "Το SENDGRID_FROM_EMAIL δεν έχει οριστεί."

        payload = {
            "personalizations": [
                {
                    "to": [
                        {
                            "email": to
                        }
                    ]
                }
            ],
            "from": {
                "email": self.sendgrid_from_email
            },
            "subject": subject,
            "content": [
                {
                    "type": "text/plain",
                    "value": body
                }
            ]
        }

        request = urllib.request.Request(
            "https://api.sendgrid.com/v3/mail/send",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.sendgrid_api_key}",
                "Content-Type": "application/json"
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status in [200, 202]:
                    return True, f"Το email στάλθηκε στο {to}."

                return False, f"Το SendGrid επέστρεψε status {response.status}."
        except urllib.error.HTTPError as error:
            error_body = error.read().decode("utf-8", errors="replace")
            return False, f"Αποτυχία SendGrid ({error.code}): {error_body}"
        except Exception as error:
            return False, f"Αποτυχία αποστολής email: {error}"

    def send_email_with_smtp(self, to: str, subject: str, body: str):
        sender = self.sender

        if not self.host or not sender:
            return False, "Δεν έχει οριστεί SENDGRID_API_KEY ή SMTP configuration."

        message = EmailMessage()
        message["From"] = sender
        message["To"] = to
        message["Subject"] = subject
        message.set_content(body)

        try:
            with smtplib.SMTP(self.host, self.port) as smtp:
                smtp.starttls()
                if self.username and self.password:
                    smtp.login(self.username, self.password)
                smtp.send_message(message)

            return True, f"Το email στάλθηκε στο {to}."
        except Exception as error:
            return False, f"Αποτυχία αποστολής email: {error}"
