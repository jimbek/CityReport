# Περιγράφει την κατηγορία ενός προβλήματος
class Category:
    def __init__(self, id: int, label: str):
        self.id = id
        self.label = label  

    def to_dict(self):
        return {
            'id': self.id,
            'label': self.label
        }

    @staticmethod
    def from_tuple(data: tuple):
        return Category(
            id = data[0],
            label = data[1]
         )
    
    @staticmethod
    def from_dict(data: dict):
        category = Category(
            id = data['id'],
            label = data['label']
        )

        return category