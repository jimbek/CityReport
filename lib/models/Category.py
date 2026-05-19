# Describes the category of a problem.
class Category:
    def __init__(self, id: int, label: str):
        self.id = id
        self.label = label  

    # Converts a database row to a dictionary.
    @staticmethod
    def to_dict(row: tuple = None):
        if row is None:
            return None
        
        return {
            'id': row[0],
            'label': row[1]
        }