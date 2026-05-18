# Περιγράφει το πρόβλημα που καταχωρεί ο πολίτης
class Problem:
    def __init__(self, id: str, categoryId: int, stateId: int, title: str, description: str, latitude: float, longitude: float, createdAt: str, updatedAt: str):
        self.id = id
        self.categoryId = categoryId
        self.stateId = stateId
        self.title = title
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.createdAt = createdAt
        self.updatedAt = updatedAt

        self.category = None
        self.state = None

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            'category': self.category,
            'state': self.state
        }
    
    @staticmethod
    def from_tuple(data: tuple):
        problem = Problem(
            id = data[0],
            categoryId = data[1],
            stateId = data[2],
            title = data[3],
            description = data[4],
            latitude = data[5],
            longitude = data[6],
            createdAt = data[7],
            updatedAt = data[8]
        )
        problem.category = {'id': data[9], 'label': data[10]} if len(data) > 9 else None
        problem.state = {'id': data[11], 'label': data[12]} if len(data) > 11 else None

        return problem
    
    @staticmethod
    def from_dict(data: dict):
        problem = Problem(
            id = data['id'],
            categoryId = data['categoryId'],
            stateId = data['stateId'],
            title = data['title'],
            description = data['description'],
            latitude = data['latitude'],
            longitude = data['longitude'],
            createdAt = data['createdAt'],
            updatedAt = data['updatedAt']
        )

        problem.category = data.get('category', None)
        problem.state = data.get('state', None)

        return problem