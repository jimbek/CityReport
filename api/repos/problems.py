# Υλοποιεί το repository για τα προβλήματα
import datetime

from repos.base import BaseRepository
from models.Problem import Problem

class ProblemsRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def apply_migrations(self):
        super().apply_migrations('''
            CREATE TABLE IF NOT EXISTS problems (
                id TEXT PRIMARY KEY,
                categoryId INTEGER,
                stateId INTEGER,
                title TEXT,
                description TEXT,
                latitude REAL,
                longitude REAL,
                createdAt TEXT,
                updatedAt TEXT
            )
        ''')

    def get_all_problems(self, categoryId: int = None, stateId: int = None, sortBy: str = None):
        query = 'SELECT * FROM problems'

        if categoryId is not None and categoryId > 0:
            query += f' WHERE categoryId = {categoryId}'

        if stateId is not None and stateId > 0:
            if 'WHERE' in query:
                query += f' AND stateId = {stateId}'
            else:
                query += f' WHERE stateId = {stateId}'
        
        if sortBy is not None:
            query += f' ORDER BY {sortBy}'

        data = self.sql_get_all(query)
        
        problems = [Problem.from_tuple(row).to_dict() for row in data]

        return problems

    def get_problem_by_id(self, id: str):
        query = f'SELECT * FROM problems WHERE id = "{id}"'

        data = self.sql_get_one(query)

        problem = Problem.from_tuple(data) if data is not None else None
        problem = problem.to_dict() if problem is not None else None

        return problem

    def add_problem(self, data: dict):
        problem = Problem.from_dict(data)

        self.sql_command(f'INSERT INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("{problem.id}", {problem.categoryId}, {problem.stateId}, "{problem.title}", "{problem.description}", {problem.latitude}, {problem.longitude}, "{problem.createdAt}", "{problem.updatedAt}")')
        
        return problem.id
    
    def update_problem(self, id: str, data: dict):
        problem_in_db = self.get_problem_by_id(id)

        if problem_in_db is None:
            return None
        
        data['id'] = id
        data['createdAt'] = problem_in_db['createdAt']

        data['updatedAt'] = datetime.datetime.now().isoformat()

        data['categoryId'] = data.get('categoryId', problem_in_db['categoryId'])
        data['stateId'] = data.get('stateId', problem_in_db['stateId'])
        data['title'] = data.get('title', problem_in_db['title'])
        data['description'] = data.get('description', problem_in_db['description'])
        data['latitude'] = data.get('latitude', problem_in_db['latitude'])
        data['longitude'] = data.get('longitude', problem_in_db['longitude'])

        problem = Problem.from_dict(data)
        query = f'UPDATE problems SET categoryId = {problem.categoryId}, stateId = {problem.stateId}, title = "{problem.title}", description = "{problem.description}", latitude = {problem.latitude}, longitude = {problem.longitude}, updatedAt = "{problem.updatedAt}" WHERE id = "{id}"'

        self.sql_command(query)

        return id
    
    def delete_problem(self, id: str):
        problem_in_db = self.get_problem_by_id(id)

        if problem_in_db is None:
            return False

        self.sql_command(f'DELETE FROM problems WHERE id = "{id}"')

        return True