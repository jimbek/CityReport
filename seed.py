# Applies database migrations and seeds the database with initial data.
from lib.repos.StatesRepository import StatesRepository
from lib.repos.CategoriesRepository import CategoriesRepository
from lib.repos.ProblemsRepository import ProblemsRepository
from lib.repos.CommentsRepository import CommentsRepository

states_repo = StatesRepository()
categories_repo = CategoriesRepository()
problems_repo = ProblemsRepository()
comments_repo = CommentsRepository()

if states_repo.table_exists('states') is False:
    states_repo.apply_migrations()
    states_repo.seed_db()

if categories_repo.table_exists('categories') is False:
    categories_repo.apply_migrations()
    categories_repo.seed_db()

if problems_repo.table_exists('problems') is False:
    problems_repo.apply_migrations()
    problems_repo.seed_db()

if comments_repo.table_exists('comments') is False:
    comments_repo.apply_migrations()
    comments_repo.seed_db()