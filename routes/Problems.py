# Defines the routes for the Problems resource.
import datetime
import uuid

from flask import request

from lib.repos.CommentsRepository import CommentsRepository
from lib.repos.StatesRepository import StatesRepository
from lib.repos.ProblemsRepository import ProblemsRepository

# Initialize the repository, apply migrations, and seed the database.
repo = ProblemsRepository()
repo.apply_migrations()
repo.seed_db()

comments_repo = CommentsRepository()

# GET /problems?categoryId=<string:categoryId>&stateId=<string:stateId>&sortBy=<string:sortBy>
# Get all problems, optionally filtered by categoryId and stateId, and sorted by createdAt or updatedAt.
def get_problems():
    categoryId = request.args.get('categoryId')
    stateId = request.args.get('stateId')
    sortBy = request.args.get('sortBy')

    if sortBy is not None and sortBy != '' and sortBy not in ['createdAt', 'updatedAt']:
        return "Invalid sortBy value, it can take 'createdAt' or 'updatedAt'", 400

    return repo.get_all_problems(categoryId, stateId, sortBy), 200

# GET /problems/<string:id> - Get a problem by ID.
def get_problem(id : str):
    problem = repo.get_problem_by_id(id)

    if problem is None:
        return "Problem not found", 404
    
    return problem, 200

# POST /problems - Create a new problem.
def create_problem():
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    if not data.get("categoryId") or not data.get("title") or not data.get("description") or not data.get("latitude") or not data.get("longitude"):
        return "Missing parameters", 400

    data['id'] = str(uuid.uuid4())

    data['stateId'] = StatesRepository.DEFAULT_STATE # Default state ID for "Νέο"

    data['createdAt'] = data['updatedAt'] = datetime.datetime.now().isoformat()

    return repo.add_problem(data), 201

# PUT /problems/<string:id> - Update a problem by ID.
def update_problem(id: str):
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    found = repo.update_problem(id, data)

    if not found:
        return "Problem not found", 404

    return id, 200

# DELETE /problems/<string:id> - Delete a problem by ID.
def delete_problem(id: str):
    problem = repo.get_problem_by_id(id)

    if problem is None:
        return "Problem not found", 404

    comments_repo.delete_comments_by_problem_id(id)
    
    repo.delete_problem(id)

    return id, 200