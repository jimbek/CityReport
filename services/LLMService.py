import json
import os
import unicodedata
import urllib.error
import urllib.request

from lib.repos.CategoriesRepository import CategoriesRepository


class LLMService:
    def __init__(self):
        self.categories_repo = CategoriesRepository()
        self.ollama_url = os.getenv("OLLAMA_URL")
        self.ollama_model = os.getenv("OLLAMA_MODEL")

    def validate_category(self, id: str, title: str, description: str):
        selected_category = self.categories_repo.get_category_by_id(id)

        if selected_category is None:
            return {
                "is_valid": False,
                "selected_category": "",
                "predicted_category": "",
                "message": "Η επιλεγμένη κατηγορία δεν βρέθηκε."
            }

        predicted_category = self.predict_category(title, description)

        if predicted_category is None:
            return {
                "is_valid": False,
                "selected_category": selected_category["label"],
                "predicted_category": "",
                "message": "Δεν ήταν δυνατή η επικοινωνία με το Ollama."
            }

        return {
            "is_valid": self.normalize_text(selected_category["label"]) == self.normalize_text(predicted_category),
            "selected_category": selected_category["label"],
            "predicted_category": predicted_category,
            "message": ""
        }

    def predict_category(self, title: str, description: str):
        categories = self.categories_repo.get_all_categories()
        category_labels = [category["label"] for category in categories]

        prompt = f"""
You classify city issue reports into exactly one category.

Allowed categories:
{", ".join(category_labels)}

Problem title:
{title}

Problem description:
{description}

Return only one category from the allowed categories.
Do not explain your answer.
"""

        payload = {
            "model": self.ollama_model,
            "prompt": prompt,
            "stream": False
        }

        request = urllib.request.Request(
            self.ollama_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                response_data = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            return None

        ollama_answer = response_data.get("response", "").strip()

        return self.match_category(ollama_answer, category_labels)

    def match_category(self, ollama_answer: str, category_labels: list[str]):
        normalized_answer = self.normalize_text(ollama_answer)

        for category_label in category_labels:
            if self.normalize_text(category_label) == normalized_answer:
                return category_label

        for category_label in category_labels:
            if self.normalize_text(category_label) in normalized_answer:
                return category_label

        return None

    def normalize_text(self, text: str):
        text_without_tones = ''.join(
            character for character in unicodedata.normalize("NFD", text or "")
            if unicodedata.category(character) != "Mn"
        )

        return text_without_tones.casefold().strip()
