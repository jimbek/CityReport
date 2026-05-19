# This page allows admins to edit existing problems.
# It retrieves the problem's current data and pre-fills the form fields.
import streamlit as st

from lib.repos.CategoriesRepository import CategoriesRepository
from lib.repos.ProblemsRepository import ProblemsRepository
from lib.repos.StatesRepository import StatesRepository

# Initialize a container for the page content.
container = st.container()
container.header("Επεξεργασία")

states_repo = StatesRepository()
categories_repo = CategoriesRepository()
problems_repo = ProblemsRepository()

all_states = states_repo.get_all_states()
all_categories = categories_repo.get_all_categories()

problem = problems_repo.get_problem_by_id(st.query_params.get('problemId', ['']))

# Initialize a form for editing the problem.
with st.form("edit_form"):

    # Helper function to get the label for a given state ID.
    def get_state_label(state_id):
        return next(state['label'] for state in all_states if state['id'] == state_id)
    
    # Helper function to get the label for a given category ID.
    def get_category_label(category_id):
        return next(category['label'] for category in all_categories if category['id'] == category_id)

    title = st.text_input("Τίτλος", value = problem['title'])
    description = st.text_area("Περιγραφή", value = problem['description'])

    longitude = st.number_input("Γεωγραφικό μήκος", value = problem['longitude'], format="%.6f")
    latitude = st.number_input("Γεωγραφικό πλάτος", value = problem['latitude'], format="%.6f")

    # Pre-select the current state in the dropdown.
    state_id = st.selectbox(
        "Κατάτασταση",
        index = next(i for i, state in enumerate(all_states) if state['id'] == problem['state']['id']),
        options = list(state['id'] for state in all_states), format_func = lambda x: get_state_label(x))
    
    # Pre-select the current category in the dropdown.
    category_id = st.selectbox(
        "Κατηγορία",
        index = next(i for i, category in enumerate(all_categories) if category['id'] == problem['category']['id']),
        options = list(category['id'] for category in all_categories), format_func = lambda x: get_category_label(x))
    
    submit_button = st.form_submit_button(label = "Ενημέρωση", type = "tertiary", icon = ":material/save:")

    # Handle form submission: update the problem with the new data and navigate back to the index page.
    if submit_button:

        # Create an updated problem object with the new values from the form.
        problem = {
            "id": problem['id'],
            "stateId": state_id,
            "categoryId": category_id,
            "title": title,
            "description": description,
            "longitude": longitude,
            "latitude": latitude
        }

        problems_repo.update_problem(problem['id'], problem)

        st.switch_page("pages/index.py")