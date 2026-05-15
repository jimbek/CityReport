# Δηλώνουμε τα routes για τις καταστάσεις των προβλημάτων
import uuid

from flask import request

from repos.States import StatesRepository

repo = StatesRepository()

def get_states():
    return repo.get_all_states(), 200

def get_state(id : str):
    state = repo.get_state_by_id(id)

    if state is None:
        return "State not found", 404
    
    return state, 200

def create_state():
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    if not data.get("label"):
        return "Missing parameters", 400
    
    data['id'] = str(uuid.uuid4())

    return repo.add_state(data), 201

def update_state(id: str):
    data = request.get_json()

    if data is None:
        return "Body is missing", 400
    
    if not data.get("label"):
        return "Missing parameters", 400
    
    found = repo.update_state(id, data)

    if not found:
        return "State not found", 404

    return id, 200

def delete_state(id: str):
    found = repo.delete_state(id)

    if not found:
        return "State not found", 404

    return id, 200