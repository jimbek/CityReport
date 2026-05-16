# Περιγράφει το σχόλιο που μπορεί να προστεθεί σε ένα πρόβλημα
class Comment:
    def __init__(self, id: str, problemId: str, author: str, content: str, createdAt: str):
        self.id = id
        self.problemId = problemId
        self.author = author
        self.content = content
        self.createdAt = createdAt
    
    def to_dict(self):
        return {
            'id': self.id,
            'problemId': self.problemId,
            'author': self.author,
            'content': self.content,
            'createdAt': self.createdAt
        }

    @staticmethod
    def from_tuple(data: tuple):
        return Comment(
            id=data[0],
            problemId=data[1],
            author=data[2],
            content=data[3],
            createdAt=data[4]
        )

    @staticmethod
    def from_dict(data: dict):
        return Comment(
            id=data.get('id'),
            problemId=data.get('problemId'),
            author=data.get('author'),
            content=data.get('content'),
            createdAt=data.get('createdAt')
        )