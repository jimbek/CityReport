# Defines the routes for the Category resource.
from lib.repos.CategoriesRepository import CategoriesRepository

# Initialize the repository, apply migrations, and seed the database with initial data.
repo = CategoriesRepository()
repo.apply_migrations()
repo.seed_db()

# GET /categories - Get all categories.
def get_categories():
    try:
        return repo.get_all_categories(), 200
    except Exception as error:
        return f"Internal server error: {error}", 500

# GET /categories/<string:id> - Get a category by ID.
def get_category(id : str):
    try:
        category = repo.get_category_by_id(id)

        if category is None:
            return "Category not found", 404
        
        return category, 200
    except Exception as error:
        return f"Internal server error: {error}", 500
