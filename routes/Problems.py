# Defines the routes for the Problems resource.
import datetime
import uuid

from flask import request

from lib.repos.CategoriesRepository import CategoriesRepository
from lib.repos.CommentsRepository import CommentsRepository
from lib.repos.StatesRepository import StatesRepository
from lib.repos.ProblemsRepository import ProblemsRepository

# Initialize the repository, apply migrations, and seed the database.
repo = ProblemsRepository()
repo.apply_migrations()
repo.seed_db()

categories_repo = CategoriesRepository()
states_repo = StatesRepository()
comments_repo = CommentsRepository()

# GET /problems?categoryId=<string:categoryId>&stateId=<string:stateId>&sortBy=<string:sortBy>
# Get all problems, optionally filtered by categoryId and stateId, and sorted by createdAt or updatedAt.
def get_problems():
    categoryId = request.args.get('categoryId')
    stateId = request.args.get('stateId')
    sortBy = request.args.get('sortBy')

    if sortBy is not None and sortBy != '' and sortBy not in ['createdAt', 'updatedAt']:
        return "Invalid sortBy value, it can take 'createdAt' or 'updatedAt'", 400
    
    if categoryId is not None and categoryId != '' and not categories_repo.category_exists(categoryId):
        return "Category not found", 404

    if stateId is not None and stateId != '' and not states_repo.state_exists(stateId):
        return "State not found", 404

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

    if data.get("categoryId") is not None and data.get("categoryId") != '' and not categories_repo.category_exists(data.get("categoryId")):
        return "Category not found", 404

    data['id'] = str(uuid.uuid4())

    data['stateId'] = StatesRepository.DEFAULT_STATE # Default state ID for "Νέο"

    data['createdAt'] = data['updatedAt'] = datetime.datetime.now().isoformat()

    data['reportedByEmail'] = data.get('reportedByEmail', '')

    return repo.add_problem(data), 201

# PUT /problems/<string:id> - Update a problem by ID.
def update_problem(id: str):
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    if data.get("categoryId") is not None and data.get("categoryId") != '' and not categories_repo.category_exists(data.get("categoryId")):
        return "Category not found", 404

    if data.get("stateId") is not None and data.get("stateId") != '' and not states_repo.state_exists(data.get("stateId")):
        return "State not found", 404

    found = repo.update_problem(id, data)

    if not found:
        return "Problem not found", 404

    return id, 200

# DELETE /problems/<string:id> - Delete a problem by ID.
def delete_problem(id: str):
    found = repo.problem_exists(id)

    if not found:
        return "Problem not found", 404

    comments_repo.delete_comments_by_problem_id(id)
    
    repo.delete_problem(id)

    return id, 200