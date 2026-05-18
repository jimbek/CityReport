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

def show_problems(stateId: str, categoryId: str):
    global container
    
    problems = problems_repo.get_all_problems(categoryId, stateId)

    if not problems:
        container.write("Δεν βρέθηκαν προβλήματα με τα επιλεγμένα κριτήρια.")
        return

    titles = []
    descriptions = []
    longitudes = []
    latitudes = []
    created_at = []
    updated_at = []
    actions = []

    for problem in problems:
        titles.append(problem['title'])
        descriptions.append(problem['description'])
        longitudes.append(problem['longitude'])
        latitudes.append(problem['latitude'])
        created_at.append(problem['createdAt'])
        updated_at.append(problem['updatedAt'])
        actions.append(f"[Επεξεργασία](edit?problemId={problem['id']})")

    confusion_matrix = pd.DataFrame(
    {
        "Τίτλος": titles,
        "Περιγραφή": descriptions,
        "Γεωγραφικό μήκος": longitudes,
        "Γεωγραφικό πλάτος": latitudes,
        "Καταχώρηση": created_at,
        "Τελευταία ενημέρωση": updated_at,
        "Ενέργειες": actions
    }
)
    container.table(confusion_matrix)

with st.sidebar:
    st.subheader("Επιλογές")

    def get_state_label(state_id):
        return next(state['label'] for state in all_states if state['id'] == state_id)
    
    def get_category_label(category_id):
        return next(category['label'] for category in all_categories if category['id'] == category_id)

    selected_state_id = st.selectbox("Κατάτασταση:", options = list(state['id'] for state in all_states), format_func = lambda x: get_state_label(x))
    selected_category_id = st.selectbox("Κατηγορία:", options = list(category['id'] for category in all_categories), format_func = lambda x: get_category_label(x))

    show_problems(selected_state_id, selected_category_id)