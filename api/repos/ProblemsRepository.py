# Υλοποιεί το repository για τα προβλήματα
import datetime

from repos.BaseRepository import BaseRepository
from models.Problem import Problem

class ProblemsRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def apply_migrations(self):
        super().apply_migrations('''
            CREATE TABLE IF NOT EXISTS problems (
                id TEXT PRIMARY KEY,
                categoryId TEXT,
                stateId TEXT,
                title TEXT,
                description TEXT,
                latitude REAL,
                longitude REAL,
                createdAt TEXT,
                updatedAt TEXT,
                FOREIGN KEY (categoryId) REFERENCES categories(id),
                FOREIGN KEY (stateId) REFERENCES states(id)
            )
        ''')

    def seed_db(self):
        super().seed_db('''
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e080", "31625a2a-a9a3-41a9-9412-c5705341e070", "31625a2a-a9a3-41a9-9412-c5705341e060", "Σπασμένος κάδος απορριμμάτων", "Ο κάδος απορριμμάτων στη γωνία των οδών Α και Β είναι σπασμένος και χρειάζεται αντικατάσταση.", 37.9838, 23.7275, "2024-01-01T10:00:00", "2024-01-01T10:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e081", "31625a2a-a9a3-41a9-9412-c5705341e071", "31625a2a-a9a3-41a9-9412-c5705341e060", "Κατεστραμμένος φωτισμός δρόμου", "Ο φωτισμός στο δρόμο Γ είναι κατεστραμμένος και δεν λειτουργεί τη νύχτα.", 37.9840, 23.7280, "2024-01-02T12:00:00", "2024-01-02T12:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e082", "31625a2a-a9a3-41a9-9412-c5705341e072", "31625a2a-a9a3-41a9-9412-c5705341e061", "Βλάβη στο δίκτυο ύδρευσης", "Υπάρχει διαρροή στο δίκτυο ύδρευσης στην περιοχή Δ που προκαλεί πλημμύρα.", 37.9845, 23.7285, "2024-01-03T14:00:00", "2024-01-03T14:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e083", "31625a2a-a9a3-41a9-9412-c5705341e073", "31625a2a-a9a3-41a9-9412-c5705341e062", "Συσσώρευση απορριμμάτων", "Υπάρχει συσσώρευση απορριμμάτων στην περιοχή Ε που προκαλεί δυσοσμία.", 37.9850, 23.7290, "2024-01-04T16:00:00", "2024-01-04T16:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e084", "31625a2a-a9a3-41a9-9412-c5705341e074", "31625a2a-a9a3-41a9-9412-c5705341e063", "Παράνομη στάθμευση", "Υπάρχει παράνομη στάθμευση στην περιοχή Ζ που εμποδίζει την κυκλοφορία.", 37.9855, 23.7295, "2024-01-05T18:00:00", "2024-01-05T18:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e085", "31625a2a-a9a3-41a9-9412-c5705341e070", "31625a2a-a9a3-41a9-9412-c5705341e060", "Καθαριότητα πεζοδρομίου", "Το πεζοδρόμιο στην περιοχή Η είναι γεμάτο σκουπίδια και χρειάζεται καθαρισμό.", 37.9860, 23.7300, "2024-01-06T20:00:00", "2024-01-06T20:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e086", "31625a2a-a9a3-41a9-9412-c5705341e071", "31625a2a-a9a3-41a9-9412-c5705341e061", "Κατεστραμμένος φωτισμός πάρκου", "Ο φωτισμός στο πάρκο Θ είναι κατεστραμμένος και δεν λειτουργεί τη νύχτα.", 37.9865, 23.7305, "2024-01-07T22:00:00", "2024-01-07T22:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e087", "31625a2a-a9a3-41a9-9412-c5705341e072", "31625a2a-a9a3-41a9-9412-c5705341e062", "Βλάβη στο δίκτυο ηλεκτροδότησης", "Υπάρχει βλάβη στο δίκτυο ηλεκτροδότησης στην περιοχή Ι που προκαλεί διακοπή ρεύματος.", 37.9870, 23.7310, "2024-01-08T09:00:00", "2024-01-08T09:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e088", "31625a2a-a9a3-41a9-9412-c5705341e073", "31625a2a-a9a3-41a9-9412-c5705341e063", "Συσσώρευση απορριμμάτων σε κάδο", "Υπάρχει συσσώρευση απορριμμάτων σε κάδο στην περιοχή Κ που προκαλεί δυσοσμία.", 37.9875, 23.7315, "2024-01-09T11:00:00", "2024-01-09T11:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e089", "31625a2a-a9a3-41a9-9412-c5705341e074", "31625a2a-a9a3-41a9-9412-c5705341e060", "Παράνομη στάθμευση σε πεζοδρόμιο", "Υπάρχει παράνομη στάθμευση σε πεζοδρόμιο στην περιοχή Λ που εμποδίζει την κυκλοφορία των πεζών.", 37.9880, 23.7320, "2024-01-10T13:00:00", "2024-01-10T13:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e08a", "31625a2a-a9a3-41a9-9412-c5705341e070", "31625a2a-a9a3-41a9-9412-c5705341e061", "Καθαριότητα παιδικής χαράς", "Η παιδική χαρά Μ είναι γεμάτη σκουπίδια και χρειάζεται καθαρισμό.", 37.9885, 23.7325, "2024-01-11T15:00:00", "2024-01-11T15:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e08b", "31625a2a-a9a3-41a9-9412-c5705341e071", "31625a2a-a9a3-41a9-9412-c5705341e062", "Κατεστραμμένος φωτισμός πεζοδρομίου", "Ο φωτισμός στο πεζοδρόμιο Ν είναι κατεστραμμένος και δεν λειτουργεί τη νύχτα.", 37.9890, 23.7330, "2024-01-12T17:00:00", "2024-01-12T17:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e08c", "31625a2a-a9a3-41a9-9412-c5705341e072", "31625a2a-a9a3-41a9-9412-c5705341e063", "Βλάβη στο δίκτυο αποχέτευσης", "Υπάρχει βλάβη στο δίκτυο αποχέτευσης στην περιοχή Ξ που προκαλεί πλημμύρα.", 37.9895, 23.7335, "2024-01-13T19:00:00", "2024-01-13T19:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e08d", "31625a2a-a9a3-41a9-9412-c5705341e073", "31625a2a-a9a3-41a9-9412-c5705341e060", "Συσσώρευση απορριμμάτων σε πάρκο", "Υπάρχει συσσώρευση απορριμμάτων σε πάρκο στην περιοχή Ο που προκαλεί δυσοσμία.", 37.9900, 23.7340, "2024-01-14T21:00:00", "2024-01-14T21:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e08e", "31625a2a-a9a3-41a9-9412-c5705341e074", "31625a2a-a9a3-41a9-9412-c5705341e061", "Παράνομη στάθμευση σε πάρκο", "Υπάρχει παράνομη στάθμευση σε πάρκο στην περιοχή Π που εμποδίζει την κυκλοφορία.", 37.9905, 23.7345, "2024-01-15T23:00:00", "2024-01-15T23:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e08f", "31625a2a-a9a3-41a9-9412-c5705341e070", "31625a2a-a9a3-41a9-9412-c5705341e062", "Καθαριότητα δρόμου", "Ο δρόμος Ρ είναι γεμάτος σκουπίδια και χρειάζεται καθαρισμό.", 37.9910, 23.7350, "2024-01-16T08:00:00", "2024-01-16T08:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e090", "31625a2a-a9a3-41a9-9412-c5705341e071", "31625a2a-a9a3-41a9-9412-c5705341e063", "Κατεστραμμένος φωτισμός σε πάρκινγκ", "Ο φωτισμός στο πάρκινγκ Σ είναι κατεστραμμένος και δεν λειτουργεί τη νύχτα.", 37.9915, 23.7355, "2024-01-17T10:00:00", "2024-01-17T10:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e091", "31625a2a-a9a3-41a9-9412-c5705341e072", "31625a2a-a9a3-41a9-9412-c5705341e060", "Βλάβη σε δημόσιο κτίριο", "Υπάρχει βλάβη σε δημόσιο κτίριο στην περιοχή Τ που χρειάζεται επισκευή.", 37.9920, 23.7360, "2024-01-18T12:00:00", "2024-01-18T12:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e092", "31625a2a-a9a3-41a9-9412-c5705341e073", "31625a2a-a9a3-41a9-9412-c5705341e061", "Συσσώρευση απορριμμάτων σε πεζοδρόμιο", "Υπάρχει συσσώρευση απορριμμάτων σε πεζοδρόμιο στην περιοχή Υ που προκαλεί δυσοσμία.", 37.9925, 23.7365, "2024-01-19T14:00:00", "2024-01-19T14:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e093", "31625a2a-a9a3-41a9-9412-c5705341e074", "31625a2a-a9a3-41a9-9412-c5705341e062", "Παράνομη στάθμευση σε πεζοδρόμιο", "Υπάρχει παράνομη στάθμευση σε πεζοδρόμιο στην περιοχή Ζ που εμποδίζει την κυκλοφορία των πεζών.", 37.9930, 23.7370, "2024-01-20T16:00:00", "2024-01-20T16:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e094", "31625a2a-a9a3-41a9-9412-c5705341e070", "31625a2a-a9a3-41a9-9412-c5705341e063", "Καθαριότητα σε δημόσιο χώρο", "Ο δημόσιος χώρος Φ είναι γεμάτος σκουπίδια και χρειάζεται καθαρισμό.", 37.9935, 23.7375, "2024-01-21T18:00:00", "2024-01-21T18:00:00");
            INSERT OR IGNORE INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e095", "31625a2a-a9a3-41a9-9412-c5705341e071", "31625a2a-a9a3-41a9-9412-c5705341e060", "Κατεστραμμένος φωτισμός σε πεζοδρόμιο", "Ο φωτισμός στο πεζοδρόμιο Χ είναι κατεστραμμένος και δεν λειτουργεί τη νύχτα.", 37.9940, 23.7380, "2024-01-22T20:00:00", "2024-01-22T20:00:00");
        ''')

    def get_all_problems(self, categoryId: str = None, stateId: str = None, sortBy: str = None):
        query = 'SELECT * FROM problems'

        if categoryId is not None and categoryId != '':
            query += f' WHERE categoryId = "{categoryId}"'

        if stateId is not None and stateId != '':
            if 'WHERE' in query:
                query += f' AND stateId = "{stateId}"'
            else:
                query += f' WHERE stateId = "{stateId}"'
        
        if sortBy is not None:
            query += f' ORDER BY {sortBy}'

        data = self.sql_get_all(query)
        
        problems = [Problem.from_tuple(row).to_dict() for row in data]

        return problems

    def get_problem_by_id(self, id: str):
        query = f'SELECT * FROM problems WHERE id = "{id}"'

        data = self.sql_get_one(query)

        problem = Problem.from_tuple(data) if data is not None else None
        problem = problem.to_dict() if problem is not None else None

        return problem

    def add_problem(self, data: dict):
        problem = Problem.from_dict(data)

        self.sql_command(f'INSERT INTO problems (id, categoryId, stateId, title, description, latitude, longitude, createdAt, updatedAt) VALUES ("{problem.id}", "{problem.categoryId}", "{problem.stateId}", "{problem.title}", "{problem.description}", {problem.latitude}, {problem.longitude}, "{problem.createdAt}", "{problem.updatedAt}")')
        
        return problem.id
    
    def update_problem(self, id: str, data: dict):
        problem_in_db = self.get_problem_by_id(id)

        if problem_in_db is None:
            return None
        
        data['id'] = id
        data['createdAt'] = problem_in_db['createdAt']

        data['updatedAt'] = datetime.datetime.now().isoformat()

        data['categoryId'] = data.get('categoryId', problem_in_db['categoryId'])
        data['stateId'] = data.get('stateId', problem_in_db['stateId'])
        data['title'] = data.get('title', problem_in_db['title'])
        data['description'] = data.get('description', problem_in_db['description'])
        data['latitude'] = data.get('latitude', problem_in_db['latitude'])
        data['longitude'] = data.get('longitude', problem_in_db['longitude'])

        problem = Problem.from_dict(data)
        query = f'UPDATE problems SET categoryId = {problem.categoryId}, stateId = {problem.stateId}, title = "{problem.title}", description = "{problem.description}", latitude = {problem.latitude}, longitude = {problem.longitude}, updatedAt = "{problem.updatedAt}" WHERE id = "{id}"'

        self.sql_command(query)

        return id
    
    def delete_problem(self, id: str):
        problem_in_db = self.get_problem_by_id(id)

        if problem_in_db is None:
            return False

        self.sql_command(f'DELETE FROM problems WHERE id = "{id}"')

        return True