from lib.repos.CategoriesRepository import CategoriesRepository


class LLMService:
    CATEGORY_KEYWORDS = {
        "Καθαριότητα": ["καθαρι", "σκουπ", "βρωμ", "πεζοδρομ", "δημοσιο χωρο"],
        "Φωτισμός": ["φωτισ", "λαμπ", "σκοταδ", "νυχτ"],
        "Βλάβες": ["βλαβ", "διαρρο", "δικτυ", "υδρευ", "ηλεκτρο", "αποχετ", "επισκευ"],
        "Απορρίμματα": ["απορρι", "καδο", "καδ", "δυσοσμ"],
        "Παράνομη στάθμευση": ["σταθμευ", "παρκαρ", "παρκινγκ", "κυκλοφορ", "εμποδιζ"],
        "Άλλο": [],
    }

    def __init__(self):
        self.categories_repo = CategoriesRepository()
        self.categories_repo.apply_migrations()
        self.categories_repo.seed_db()

    def validate_category(self, id: str, description: str):
        category = self.categories_repo.get_category_by_id(id)

        if category is None:
            return False

        if category["label"] == "Άλλο":
            return True

        normalized_description = self._normalize(description)
        keywords = self.CATEGORY_KEYWORDS.get(category["label"], [])

        return any(keyword in normalized_description for keyword in keywords)

    def _normalize(self, text: str):
        return (text or "").lower().replace("ά", "α").replace("έ", "ε").replace("ή", "η").replace("ί", "ι").replace("ό", "ο").replace("ύ", "υ").replace("ώ", "ω")
