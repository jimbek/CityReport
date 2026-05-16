# Υλοποιεί το repository για τα σχόλια
from models.Comment import Comment

from repos.BaseRepository import BaseRepository

class CommentsRepository(BaseRepository):
    def __init__(self):
        super().__init__()
    
    def apply_migrations(self):
        super().apply_migrations('''
            CREATE TABLE IF NOT EXISTS comments (
                id TEXT PRIMARY KEY,
                problemId TEXT,
                author TEXT,
                content TEXT,
                createdAt TEXT,
                FOREIGN KEY (problemId) REFERENCES problems(id)
            )
        ''')
    
    def get_comments(self, problemId: str, size: int = 10):
        data = self.sql_get_all(f'SELECT * FROM comments WHERE problemId = "{problemId}" ORDER BY createdAt DESC LIMIT {size}')
        
        return [Comment.from_tuple(row).to_dict() for row in data]
    

    def add_comment(self, data: dict):
        comment = Comment.from_dict(data)

        self.sql_command(f'INSERT INTO comments (id, problemId, author, content, createdAt) VALUES ("{comment.id}", "{comment.problemId}", "{comment.author}", "{comment.content}", "{comment.createdAt}")')
        
        return comment.id