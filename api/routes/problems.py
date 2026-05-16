# Δηλώνουμε τα routes για τα προβλήματα
import datetime
import uuid

from flask import request

from lib.repos.ProblemsRepository import ProblemsRepository

repo = ProblemsRepository()
repo.apply_migrations()
repo.seed_db()

def get_problems():
    categoryId = request.args.get('categoryId')
    stateId = request.args.get('stateId')
    sortBy = request.args.get('sortBy')

    if sortBy is not None and sortBy not in ['createdAt', 'updatedAt']:
        return "Invalid sortBy value, it can take 'createdAt' or 'updatedAt'", 400

    return repo.get_all_problems(categoryId, stateId, sortBy), 200

def get_problem(id : str):
    problem = repo.get_problem_by_id(id)

    if problem is None:
        return "Problem not found", 404
    
    return problem, 200

def create_problem():
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    if not data.get("categoryId") or not data.get("title") or not data.get("description") or not data.get("latitude") or not data.get("longitude"):
        return "Missing parameters", 400

    data['id'] = str(uuid.uuid4())
    data['stateId'] = 1
    data['createdAt'] = data['updatedAt'] = datetime.datetime.now().isoformat()

    return repo.add_problem(data), 201

def update_problem(id: str):
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    found = repo.update_problem(id, data)

    if not found:
        return "Problem not found", 404

    return id, 200

def delete_problem(id: str):
    found = repo.delete_problem(id)

    if not found:
        return "Problem not found", 404

    return id, 200