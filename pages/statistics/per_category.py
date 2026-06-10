import pandas as pd
import streamlit as st

from pages.BackButton import show_back_button
from lib.repos.CategoriesRepository import CategoriesRepository
from lib.repos.ProblemsRepository import ProblemsRepository
from lib.repos.StatesRepository import StatesRepository

show_back_button()

states_repo = StatesRepository()
categories_repo = CategoriesRepository()
problems_repo = ProblemsRepository()

all_states = states_repo.get_all_states()
all_categories = categories_repo.get_all_categories()

global container
container = st.container()
container.text("Αποτελέσματα:")

st.markdown(
    """
<style>
    .st-emotion-cache-1w723zb {
        max-width: 90%;
    }
</style>
""",
    unsafe_allow_html=True,
)

@st.cache_data
def load_problems(categoryId: str):
    return [len(problems_repo.get_all_problems(categoryId, state['id'])) for state in all_states]

def show_statistics(categoryId: str):
    states = [state['label'] for state in all_states]
    problems = load_problems(categoryId)

    df = pd.DataFrame(
        {
            "Κατηγορία": states,
            "Προβλήματα": problems,
        }
    )

    global container
    container.bar_chart(df, x = "Κατηγορία", y = "Προβλήματα", x_label = "Κατηγορία", y_label = "Προβλήματα")

with st.sidebar:
    st.subheader("Επιλογές")

    def get_category_label(category_id):
        return next(category['label'] for category in all_categories if category['id'] == category_id)

    selected_category_id = st.selectbox(
        "Κατηγορία:",
        options = list(category['id'] for category in all_categories),
        format_func = lambda x: get_category_label(x))

    show_statistics(selected_category_id)
