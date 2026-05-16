# Δηλώνουμε τα routes για τα σχόλια
import datetime
import uuid

from flask import request

from repos.CommentsRepository import CommentsRepository
from repos.ProblemsRepository import ProblemsRepository

repo = CommentsRepository()
repo.apply_migrations()

problem_repo = ProblemsRepository()

def get_comments(problemId: str):
    if problemId is None:
        return "Missing problemId", 400

    if problem_repo.get_problem_by_id(problemId) is None:
        return "Problem not found", 404

    size = request.args.get('size', default = 10, type = int)

    return repo.get_comments(problemId, size), 200

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