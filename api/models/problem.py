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
    
    def __str__(self):
        return f'Problem(id={self.id}, categoryId={self.categoryId}, stateId={self.stateId}, title={self.title}, description={self.description}, latitude={self.latitude}, longitude={self.longitude}, createdAt={self.createdAt}, updatedAt={self.updatedAt})'

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
    
    @staticmethod
    def from_tuple(data: tuple):
        return Problem(
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

        problem.id = data['id']

        return problem