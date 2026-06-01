# Applies database migrations and seeds the database with initial data.
from lib.repos.StatesRepository import StatesRepository
from lib.repos.CategoriesRepository import CategoriesRepository
from lib.repos.ProblemsRepository import ProblemsRepository

states_repo = StatesRepository()
categories_repo = CategoriesRepository()
problems_repo = ProblemsRepository()

states_repo.apply_migrations()
states_repo.seed_db()

categories_repo.apply_migrations()
categories_repo.seed_db()

problems_repo.apply_migrations()
problems_repo.seed_db()