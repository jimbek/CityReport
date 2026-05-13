# Δηλώνουμε τα routes για τα προβλήματα
from flask import request

from models.problem import Problem

def get_problems():
    categoryId = request.args.get('categoryId')
    stateId = request.args.get('stateId')
    sortBy = request.args.get('sortBy')

    return [ Problem(1, categoryId, stateId, "Title", "Description", 0.0, 0.0, "2024-01-01", "2024-01-01").to_dict() ], 200

def get_problem(id):
    return Problem(id, 1, 1, "Title", "Description", 0.0, 0.0, "2024-01-01", "2024-01-01").to_dict(), 200

def create_problem():
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    if not data.get("categoryId") or not data.get("title") or not data.get("description") or not data.get("latitude") or not data.get("longitude"):
        return "Missing parameters", 400
    
    problem = Problem(
        id=0,  # This will be set by the database
        categoryId=data["categoryId"],
        stateId=1,  # Default state (e.g., "New")
        title=data["title"],
        description=data["description"],
        latitude=data["latitude"],
        longitude=data["longitude"],
        createdAt="2024-01-01",  # This should be set to the current date/time
        updatedAt="2024-01-01"   # This should be set to the current date/time
    )

    return problem.id, 201

def update_problem(id):
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    # Here you would typically fetch the existing problem from the database,
    # update its fields with the new data, and save it back to the database.

    return id, 200