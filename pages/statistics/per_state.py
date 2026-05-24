# This is the page for displaying statistics of problems per state.
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

# Initialize a container for the page content.
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

# Function to load the number of problems for each category based on the selected state, with caching to improve performance.
@st.cache_data
def load_problems(stateId: str):
    return [len(problems_repo.get_all_problems(category['id'], stateId)) for category in all_categories]

# Function to display a histogram of the number of problems per category for the selected state.
def show_statistics(stateId: str):
    # Horizontal labels
    categories = [category['label'] for category in all_categories]

    # Vertical values
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

    # Helper function to get the label for a given state ID.
    def get_state_label(state_id):
        return next(state['label'] for state in all_states if state['id'] == state_id)

    selected_state_id = st.selectbox("Κατάτασταση:", options = list(state['id'] for state in all_states), format_func = lambda x: get_state_label(x))

    show_statistics(selected_state_id)
