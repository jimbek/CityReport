# Defines the routes for the State resource.
from lib.repos.StatesRepository import StatesRepository

# Initialize the repository, apply migrations, and seed the database.
repo = StatesRepository()
repo.apply_migrations()
repo.seed_db()

# GET /states - Get all states.
def get_states():
    return repo.get_all_states(), 200

# GET /states/<id> - Get a state by ID.
def get_state(id : str):
    state = repo.get_state_by_id(id)

    if state is None:
        return "State not found", 404
    
    return state, 200