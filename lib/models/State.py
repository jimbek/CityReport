# Describes the state of a problem.
class State:
    def __init__(self, id: str, label: str):
        self.id = id
        self.label = label

    # Converts a database row into a dictionary.
    @staticmethod
    def to_dict(data: tuple):
        return {
            'id': data[0],
            'label': data[1]
        }