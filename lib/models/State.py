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

    @staticmethod
    def from_tuple(data: tuple):
        return State(
            id = data[0],
            label = data[1]
        )

    @staticmethod
    def from_dict(data: dict):
        return State(
            id = data.get("id", 0),
            label = data.get("label", "")
        )