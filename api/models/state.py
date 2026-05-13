# Περιγράφει την κατάσταση ενός προβλήματος
class State:
    def __init__(self, id: int, label: str):
        self.id = id
        self.label = label

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label
        }

    def from_dict(self, data):
        self.id = data.get("id", self.id)
        self.label = data.get("label", self.label)