# Defines the routes for the State resource.
from lib.repos.StatesRepository import StatesRepository

# Initialize the repository, apply migrations, and seed the database.
repo = StatesRepository()

# GET /states - Get all states.
def get_states():
    try:
        return repo.get_all_states(), 200
    except Exception as error:
        return f"Internal server error: {error}", 500

# GET /states/<id> - Get a state by ID.
def get_state(id : str):
    try:
        state = repo.get_state_by_id(id)

        if state is None:
            return "State not found", 404
        
        return state, 200
    except Exception as error:
        return f"Internal server error: {error}", 500
