# Υλοποιεί το repository για τις κατηγορίες προβλημάτων
from lib.models.Category import Category
from lib.repos.BaseRepository import BaseRepository

class CategoriesRepository(BaseRepository):
    def __init__(self):
        super().__init__()
    
    def apply_migrations(self):
        super().apply_migrations('''
            CREATE TABLE IF NOT EXISTS categories (
                id TEXT PRIMARY KEY,
                label TEXT
            )
        ''')
    
    def seed_db(self):
        super().seed_db('''
            INSERT OR IGNORE INTO categories (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e070", "Καθαριότητα");
            INSERT OR IGNORE INTO categories (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e071", "Φωτισμός");
            INSERT OR IGNORE INTO categories (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e072", "Βλάβες");
            INSERT OR IGNORE INTO categories (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e073", "Απορρίμματα");
            INSERT OR IGNORE INTO categories (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e074", "Παράνομη στάθμευση");
        ''')
    
    def get_all_categories(self):
        data = self.sql_get_all('SELECT * FROM categories')

        categories = [Category.from_tuple(row).to_dict() for row in data]

        return categories
    
    def get_category_by_id(self, id: str):
        query = f'SELECT * FROM categories WHERE id = "{id}"'

        data = self.sql_get_one(query)

        category = Category.from_tuple(data) if data is not None else None
        category = category.to_dict() if category is not None else None

        return category
    
    def add_category(self, data: dict):
        category = Category.from_dict(data)

        self.sql_command(f'INSERT INTO categories (id, label) VALUES ("{category.id}", "{category.label}")')

        return category.id
    
    def update_category(self, id: str, data: dict):
        data['id'] = id
        category = Category.from_dict(data)
        
        query = f'UPDATE categories SET label = "{category.label}" WHERE id = "{id}"'

        self.sql_command(query)

        return id
    
    def delete_category(self, id: str):
        category_in_db = self.get_category_by_id(id)

        if category_in_db is None:
            return False

        self.sql_command(f'DELETE FROM categories WHERE id = "{id}"')

        return True