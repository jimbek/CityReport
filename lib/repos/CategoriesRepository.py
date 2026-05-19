# Implements the CategoriesRepository class, which is responsible for managing the categories in the database.
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
            INSERT OR IGNORE INTO categories (id, label) VALUES ("31625a2a-a9a3-41a9-9412-c5705341e075", "Άλλο");
        ''')
    
    # Retrieves all categories from the database.
    def get_all_categories(self):
        data = self.sql_get_all('SELECT * FROM categories')

        categories = [Category.to_dict(row) for row in data]

        return categories
    
    # Retrieves a category by its ID from the database, checking if a category with the given ID exists.
    def get_category_by_id(self, id: str):
        query = f'SELECT * FROM categories WHERE id = "{id}"'

        data = self.sql_get_one(query)

        category = Category.to_dict(data) if data is not None else None

        return category