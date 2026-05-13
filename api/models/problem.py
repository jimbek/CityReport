# Περιγράφει το πρόβλημα που καταχωρεί ο πολίτης

class Problem:
    def __init__(self, id: int, categoryId: int, stateId: int, title: str, description: str, latitude: float, longitude: float, createdAt: str, updatedAt: str):
        self.id = id
        self.categoryId = categoryId
        self.stateId = stateId
        self.title = title
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def to_dict(self):
        return {
            'id': self.id,
            'categoryId': self.categoryId,
            'stateId': self.stateId,
            'title': self.title,
            'description': self.description,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }