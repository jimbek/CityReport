# Δηλώνουμε τα routes για τις κατηγορίες
import uuid

from flask import request

from repos.CategoriesRepository import CategoriesRepository


repo = CategoriesRepository()
repo.apply_migrations()
repo.seed_db()

def get_categories():
    return repo.get_all_categories(), 200

def get_category(id : str):
    category = repo.get_category_by_id(id)

    if category is None:
        return "Category not found", 404
    
    return category, 200

def create_category():
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    if not data.get("label"):
        return "Missing parameters", 400
    
    data['id'] = str(uuid.uuid4())

    return repo.add_category(data), 201

def update_category(id: str):
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    if not data.get("label"):
        return "Missing parameters", 400
    
    found = repo.update_category(id, data)

    if not found:
        return "Category not found", 404

    return id, 200

def delete_category(id: str):
    found = repo.delete_category(id)

    if not found:
        return "Category not found", 404

    return id, 200