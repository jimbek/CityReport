# Describes a comment on a problem.
class Comment:
    def __init__(self, id: str, problemId: str, author: str, content: str, createdAt: str):
        self.id = id
        self.problemId = problemId
        self.author = author # "Πολίτης" or "Διαχειριστής"
        self.content = content
        self.createdAt = createdAt
    
    # Converts a database row to a dictionary.
    @staticmethod
    def to_dict(data: tuple):
        return {
            'id': data[0],
            'problemId': data[1],
            'author': data[2],
            'content': data[3],
            'createdAt': data[4]
        }