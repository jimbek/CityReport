from lib.repos.CategoriesRepository import CategoriesRepository
from lib.repos.CommentsRepository import CommentsRepository
from lib.repos.ProblemsRepository import ProblemsRepository
from lib.repos.StatesRepository import StatesRepository


def initialize_database():
    categories_repo = CategoriesRepository()
    states_repo = StatesRepository()
    problems_repo = ProblemsRepository()
    comments_repo = CommentsRepository()

    categories_repo.apply_migrations()
    states_repo.apply_migrations()
    problems_repo.apply_migrations()
    comments_repo.apply_migrations()

    categories_repo.seed_db()
    states_repo.seed_db()
    problems_repo.seed_db()
