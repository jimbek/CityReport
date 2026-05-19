# Describes a problem reported by a user.
class Problem:
    def __init__(self, id: str, categoryId: int, stateId: int, title: str, description: str, latitude: float, longitude: float, createdAt: str, updatedAt: str, reportedByEmail: str):
        self.id = id
        self.categoryId = categoryId
        self.stateId = stateId
        self.title = title
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.reportedByEmail = reportedByEmail # Optional email of the user who reported the problem.
        self.category = None
        self.state = None

    # Converts a database row to a dictionary.
    @staticmethod
    def to_dict(data: tuple):
        return {
            'id': data[0],
            'title': data[3],
            'description': data[4],
            'latitude': data[5],
            'longitude': data[6],
            'createdAt': data[7],
            'updatedAt': data[8],
            'reportedByEmail': data[9],
            'category': {
                'id': data[1],
                'label': data[10]
            },
            'state': {
                'id': data[2],
                'label': data[11]
            }
        }