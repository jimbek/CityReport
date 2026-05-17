import pandas as pd
import streamlit as st

from lib.repos.CategoriesRepository import CategoriesRepository
from lib.repos.ProblemsRepository import ProblemsRepository
from lib.repos.StatesRepository import StatesRepository

states_repo = StatesRepository()
categories_repo = CategoriesRepository()
problems_repo = ProblemsRepository()

all_states = states_repo.get_all_states()
all_categories = categories_repo.get_all_categories()

global container

container = st.container()
container.text("Αποτελέσματα:")

@st.cache_data
def load_problems(stateId: str):
    return [len(problems_repo.get_all_problems(stateId = stateId, categoryId = category['id'])) for category in all_categories]

def show_statistics(stateId: str):
    categories = [category['label'] for category in all_categories]
    problems = load_problems(stateId)

    df = pd.DataFrame(
        {
            "Κατηγορία": categories,
            "Προβλήματα": problems,
        }
    )

    global container
    container.bar_chart(df, x = "Κατηγορία", y = "Προβλήματα", x_label = "Κατηγορία", y_label = "Προβλήματα")

with st.sidebar:
    st.subheader("Επιλογές")

    def get_state_label(state_id):
        return next(state['label'] for state in all_states if state['id'] == state_id)

    selected_state_id = st.selectbox("Κατάτασταση:", options = list(state['id'] for state in all_states), format_func = lambda x: get_state_label(x))

    show_statistics(selected_state_id)
