import os
import json
import urllib.error
import urllib.request


class EmailService:
    def __init__(self):
        self.resend_api_key = os.getenv("RESEND_API_KEY")
        self.resend_from_email = os.getenv("RESEND_FROM_EMAIL")

    def send_email(self, to: str, subject: str, body: str):
        if not to:
            return False, "Δεν υπάρχει email παραλήπτη."

        if self.resend_api_key:
            return self.send_email_with_resend(to, subject, body)

        return False, "Δεν έχει οριστεί RESEND_API_KEY."

    def send_email_with_resend(self, to: str, subject: str, body: str):
        if not self.resend_from_email:
            return False, "Το RESEND_FROM_EMAIL δεν έχει οριστεί."

        payload = {
            "from": self.resend_from_email,
            "to": [to],
            "subject": subject,
            "text": body
        }

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
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status in [200, 201, 202]:
                    return True, f"Το email στάλθηκε στο {to}."

                return False, f"Το Resend επέστρεψε status {response.status}."
        except urllib.error.HTTPError as error:
            error_body = error.read().decode("utf-8", errors="replace")
            return False, f"Αποτυχία Resend ({error.code}): {error_body}"
        except Exception as error:
            return False, f"Αποτυχία αποστολής email: {error}"
