import streamlit as st

from lib.repos.CategoriesRepository import CategoriesRepository
from lib.repos.ProblemsRepository import ProblemsRepository
from lib.repos.StatesRepository import StatesRepository

global container
container = st.container()
container.header("Επεξεργασία")

states_repo = StatesRepository()
categories_repo = CategoriesRepository()
problems_repo = ProblemsRepository()

all_states = states_repo.get_all_states()
all_categories = categories_repo.get_all_categories()

problem = problems_repo.get_problem_by_id(st.query_params.get('problemId', ['']))

with st.form("edit_form"):
    def get_state_label(state_id):
        return next(state['label'] for state in all_states if state['id'] == state_id)
    
    def get_category_label(category_id):
        return next(category['label'] for category in all_categories if category['id'] == category_id)

    title = st.text_input("Τίτλος", value = problem['title'])
    description = st.text_area("Περιγραφή", value = problem['description'])

    longitude = st.number_input("Γεωγραφικό μήκος", value = problem['longitude'], format="%.6f")
    latitude = st.number_input("Γεωγραφικό πλάτος", value = problem['latitude'], format="%.6f")

    state_id = st.selectbox("Κατάτασταση", index = next(i for i, state in enumerate(all_states) if state['id'] == problem['state']['id']), options = list(state['id'] for state in all_states), format_func = lambda x: get_state_label(x))
    category_id = st.selectbox("Κατηγορία", index = next(i for i, category in enumerate(all_categories) if category['id'] == problem['category']['id']), options = list(category['id'] for category in all_categories), format_func = lambda x: get_category_label(x))
    
    submit_button = st.form_submit_button(label = "Ενημέρωση")