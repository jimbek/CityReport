# Implements the StatesRepository class, which is responsible for managing the states in the database.
from lib.models.State import State
from lib.repos.BaseRepository import BaseRepository

class StatesRepository(BaseRepository):
    DEFAULT_STATE = "31625a2a-a9a3-41a9-9412-c5705341e060"
    
    def __init__(self):
        super().__init__()
    
    def apply_migrations(self):
        super().apply_migrations('''
            CREATE TABLE IF NOT EXISTS states (
                id TEXT PRIMARY KEY,
                label TEXT
            )
        ''')
    
    def seed_db(self):
        super().seed_db(f'''
            INSERT OR IGNORE INTO states (id, label) VALUES ("{self.DEFAULT_STATE}", "Νέο");
            INSERT OR IGNORE INTO states (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e061", "Υπό επεξεργασία");
            INSERT OR IGNORE INTO states (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e062", "Απορριφθέν");
            INSERT OR IGNORE INTO states (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e063", "Ολοκληρωμένο");
        ''')
    
    # Retrieves all states from the database.
    def get_all_states(self):
        data = self.sql_get_all('SELECT * FROM states')

        states = [State.to_dict(row) for row in data]

        return states
    
    # Retrieves a state by its ID from the database, checking if a state with the given ID exists.
    def get_state_by_id(self, id: str):
        data = self.sql_get_one(f'SELECT * FROM states WHERE id = "{id}"')

        state = State.to_dict(data) if data is not None else None

        return state