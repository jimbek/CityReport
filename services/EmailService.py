import os
import json
import urllib.error
import urllib.request


class EmailService:
    # This service is responsible only for sending emails.
    # It uses Resend, so the API key is read from environment variables instead of being written in the code.
    def __init__(self):
        self.resend_api_key = os.getenv("RESEND_API_KEY")
        self.resend_from_email = os.getenv("RESEND_FROM_EMAIL")

    def send_email(self, to: str, subject: str, body: str):
        # If the problem has no citizen email, there is nowhere to send the message.
        if not to:
            return False, "Δεν υπάρχει email παραλήπτη."

        # If Resend is configured, send the email through the Resend API.
        if self.resend_api_key:
            return self.send_email_with_resend(to, subject, body)

        # If no API key exists, we do not crash the app. We return an error message for the UI.
        return False, "Δεν έχει οριστεί RESEND_API_KEY."

    def send_email_with_resend(self, to: str, subject: str, body: str):
        # Resend also needs a sender email. In testing this can be onboarding@resend.dev.
        if not self.resend_from_email:
            return False, "Το RESEND_FROM_EMAIL δεν έχει οριστεί."

        # This is the email data that will be sent to Resend.
        payload = {
            "from": self.resend_from_email,
            "to": [to],
            "subject": subject,
            "text": body
        }

        # This prepares the HTTP request to Resend's send-email endpoint.
        request = urllib.request.Request(
            "https://api.resend.com/emails",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.resend_api_key}",
                "Content-Type": "application/json",
                "User-Agent": "CityReport/1.0"
            },
            method="POST"
        )

        try:
            # This actually sends the request to Resend.
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status in [200, 201, 202]:
                    return True, f"Το email στάλθηκε στο {to}."

                return False, f"Το Resend επέστρεψε status {response.status}."
        except urllib.error.HTTPError as error:
            # Resend returned an HTTP error, so we read the error body to show a useful message.
            error_body = error.read().decode("utf-8", errors="replace")
            return False, f"Αποτυχία Resend ({error.code}): {error_body}"
        except Exception as error:
            # Any other unexpected email error is caught here so the app does not crash.
            return False, f"Αποτυχία αποστολής email: {error}"
