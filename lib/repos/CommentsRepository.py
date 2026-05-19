# Implements the CommentsRepository class, which is responsible for managing the comments in the database.
from lib.models.Comment import Comment
from lib.repos.BaseRepository import BaseRepository

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
    
    # Retrieves all comments for a given problem ID, ordered by creation date.
    def get_comments(self, problemId: str):
        data = self.sql_get_all(f'SELECT * FROM comments WHERE problemId = "{problemId}" ORDER BY createdAt')
        
        return [Comment.to_dict(row) for row in data]
    
    # Adds a new comment to the database and returns the ID of the newly created comment.
    def add_comment(self, data: dict):
        self.sql_command(f'INSERT INTO comments (id, problemId, author, content, createdAt) VALUES ("{data['id']}", "{data['problemId']}", "{data['author']}", "{data['content']}", "{data['createdAt']}")')
        
        return data['id']
    
    # Deletes all comments associated with a given problem ID.
    def delete_comments_by_problem_id(self, problemId: str):
        self.sql_command(f'DELETE FROM comments WHERE problemId = "{problemId}"')