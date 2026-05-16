# Υλοποιεί το repository για τις καταστάσεις των προβλημάτων
from lib.models.State import State
from lib.repos.BaseRepository import BaseRepository

class StatesRepository(BaseRepository):
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
        super().seed_db('''
            INSERT OR IGNORE INTO states (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e060", "Νέο");
            INSERT OR IGNORE INTO states (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e061", "Υπό επεξεργασία");
            INSERT OR IGNORE INTO states (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e062", "Απορριφθέν");
            INSERT OR IGNORE INTO states (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e063", "Ολοκληρωμένο");
        ''')
    
    def get_all_states(self):
        data = self.sql_get_all('SELECT * FROM states')

        states = [State.from_tuple(row).to_dict() for row in data]

        return states
    
    def get_state_by_id(self, id: str):
        query = f'SELECT * FROM states WHERE id = "{id}"'

        data = self.sql_get_one(query)

        state = State.from_tuple(data).to_dict() if data is not None else None

        return state
    
    def add_state(self, data: dict):
        state = State.from_dict(data)

        self.sql_command(f'INSERT INTO states (id, label) VALUES ("{state.id}", "{state.label}")')

        return state.id
    
    def update_state(self, id: str, data: dict):
        data['id'] = id
        state = State.from_dict(data)
        
        query = f'UPDATE states SET label = "{state.label}" WHERE id = "{id}"'

        self.sql_command(query)

        return id
    
    def delete_state(self, id: str):
        state_in_db = self.get_state_by_id(id)

        if state_in_db is None:
            return False

        self.sql_command(f'DELETE FROM states WHERE id = "{id}"')

        return True