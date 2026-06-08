import json
import os
import unicodedata
import urllib.error
import urllib.request

from lib.repos.CategoriesRepository import CategoriesRepository


class LLMService:
    # This service is responsible for asking Ollama to predict the correct problem category.
    # The edit page uses it when the admin clicks the "Έλεγχος" button.
    def __init__(self):
        # We need the category repository so we know all valid categories from the database.
        self.categories_repo = CategoriesRepository()

        # These values come from environment variables, usually configured by Docker or the terminal.
        self.ollama_url = os.getenv("OLLAMA_URL")
        self.ollama_model = os.getenv("OLLAMA_MODEL")

    def validate_category(self, id: str, title: str, description: str):
        # First we find the category that the user selected in the edit form.
        selected_category = self.categories_repo.get_category_by_id(id)

        # If the selected category id does not exist, the check cannot be valid.
        if selected_category is None:
            return {
                "is_valid": False,
                "selected_category": "",
                "predicted_category": "",
                "message": "Η επιλεγμένη κατηγορία δεν βρέθηκε."
            }

        # Ask Ollama to predict the best category from the title and description.
        predicted_category = self.predict_category(title, description)

        # If Ollama is not running or gives an invalid answer, we show a clear message.
        if predicted_category is None:
            return {
                "is_valid": False,
                "selected_category": selected_category["label"],
                "predicted_category": "",
                "message": "Δεν ήταν δυνατή η επικοινωνία με το Ollama."
            }

        # We compare the selected category with Ollama's predicted category.
        # normalize_text makes the comparison ignore capital letters and Greek tones.
        return {
            "is_valid": self.normalize_text(selected_category["label"]) == self.normalize_text(predicted_category),
            "selected_category": selected_category["label"],
            "predicted_category": predicted_category,
            "message": ""
        }

    def predict_category(self, title: str, description: str):
        # Load all allowed categories. Ollama must choose only from this list.
        categories = self.categories_repo.get_all_categories()
        category_labels = [category["label"] for category in categories]

        # This is the instruction we send to Ollama.
        # We ask it to return only one category, not a long explanation.
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

        # This is the JSON body sent to Ollama's local API.
        payload = {
            "model": self.ollama_model,
            "prompt": prompt,
            "stream": False
        }

        # This prepares the HTTP request to Ollama.
        request = urllib.request.Request(
            self.ollama_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        try:
            # This sends the request to Ollama and reads the JSON response.
            with urllib.request.urlopen(request, timeout=60) as response:
                response_data = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            # If Ollama is closed, slow, or returns bad JSON, we return None.
            return None

        # Ollama's text answer is stored in the "response" field.
        ollama_answer = response_data.get("response", "").strip()

        # Match Ollama's answer to one of our real category labels.
        return self.match_category(ollama_answer, category_labels)

    def match_category(self, ollama_answer: str, category_labels: list[str]):
        # Normalize the answer so "Φωτισμός", "φωτισμος", and "ΦΩΤΙΣΜΟΣ" match.
        normalized_answer = self.normalize_text(ollama_answer)

        # First try an exact match after normalization.
        for category_label in category_labels:
            if self.normalize_text(category_label) == normalized_answer:
                return category_label

        # If Ollama returned extra words, try to find a category inside the answer.
        for category_label in category_labels:
            if self.normalize_text(category_label) in normalized_answer:
                return category_label

        # If nothing matches, the prediction is not usable.
        return None

    def normalize_text(self, text: str):
        # Remove Greek tones/accents so comparisons are more forgiving.
        text_without_tones = ''.join(
            character for character in unicodedata.normalize("NFD", text or "")
            if unicodedata.category(character) != "Mn"
        )

        # casefold is like lower(), but stronger for text comparisons.
        return text_without_tones.casefold().strip()
