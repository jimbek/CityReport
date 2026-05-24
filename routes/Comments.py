# Defines the routes for the Comment resource.
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
    try:
        if problemId is None or problemId == '':
            return "Missing problemId", 400

        if problem_repo.problem_exists(problemId) is False:
            return "Problem not found", 404

        return repo.get_comments(problemId), 200
    except Exception as error:
        return f"Internal server error: {error}", 500

# POST /problems/<string:problemId>/comments - Create a comment for a problem.
def create_comment(problemId: str):
    try:
        if problemId is None or problemId == '':
            return "Missing problemId", 400
        
        data = request.get_json()

        if data is None:
            return "Body is missing", 400
        
        if not data.get("author") or not data.get("content"):
            return "Missing parameters", 400
        
        if "author" in data and data["author"] not in ["Πολίτης", "Διαχειριστής"]:
            return "Invalid author", 400
        
        if problem_repo.problem_exists(problemId) is False:
            return "Problem not found", 404
        
        data['problemId'] = problemId

        return repo.add_comment(data), 201
    except Exception as error:
        return f"Internal server error: {error}", 500
