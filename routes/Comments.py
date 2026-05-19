# Defines the routes for the Comment resource.
import datetime
import uuid

from flask import request

from lib.repos.CommentsRepository import CommentsRepository
from lib.repos.ProblemsRepository import ProblemsRepository

# Initialize the CommentsRepository and apply migrations.
repo = CommentsRepository()
repo.apply_migrations()

# Initialize the ProblemsRepository to check for the existence of problems when creating comments.
problem_repo = ProblemsRepository()

# GET /problems/<string:problemId>/comments - Get comments for a problem.
def get_comments(problemId: str):
    if problemId is None:
        return "Missing problemId", 400

    if problem_repo.get_problem_by_id(problemId) is None:
        return "Problem not found", 404

    return repo.get_comments(problemId), 200

# POST /problems/<string:problemId>/comments - Create a comment for a problem.
def create_comment(problemId: str):
    if problemId is None:
        return "Missing problemId", 400
    
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    if not data.get("author") or not data.get("content"):
        return "Missing parameters", 400
    
    if "author" in data and data["author"] not in ["Πολίτης", "Διαχειριστής"]:
        return "Invalid author", 400
    
    if problem_repo.get_problem_by_id(problemId) is None:
        return "Problem not found", 404
    
    data['id'] = str(uuid.uuid4())
    
    data['problemId'] = problemId

    data['createdAt'] = datetime.datetime.now().isoformat()

    return repo.add_comment(data), 201