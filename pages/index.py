# This is the main page of the application.
# Admins can view and filter problems based on their state and category.
import streamlit as st

from lib.repos.CategoriesRepository import CategoriesRepository
from lib.repos.ProblemsRepository import ProblemsRepository
from lib.repos.StatesRepository import StatesRepository

states_repo = StatesRepository()
categories_repo = CategoriesRepository()
problems_repo = ProblemsRepository()

all_states = states_repo.get_all_states()
all_categories = categories_repo.get_all_categories()

# Initialize a container for the page content.
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

# Function to display problems based on selected state and category.
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
        # Append problem details to the corresponding lists for display in the table.
        titles.append(problem['title'])
        descriptions.append(problem['description'])
        longitudes.append(problem['longitude'])
        latitudes.append(problem['latitude'])
        created_at.append(problem['createdAt'])
        updated_at.append(problem['updatedAt'])

        # Append action links in markdown format.
        actions.append(f"[:material/edit:](edit?problemId={problem['id']}) [:material/chat:](comments?problemId={problem['id']})")

    # Display the problems in a table format with an additional column for actions.
    container.table({
        "Τίτλος": titles,
        "Περιγραφή": descriptions,
        "Γεωγραφικό μήκος": longitudes,
        "Γεωγραφικό πλάτος": latitudes,
        "Καταχώρηση": created_at,
        "Τελευταία ενημέρωση": updated_at,
        "Ενέργειες": actions
    })

# Display sidebar options for filtering problems by state and category.
with st.sidebar:
    st.subheader("Επιλογές")

    # Helper function to get the label for a given state ID.
    def get_state_label(state_id):
        return next(state['label'] for state in all_states if state['id'] == state_id)
    
    # Helper function to get the label for a given category ID.
    def get_category_label(category_id):
        return next(category['label'] for category in all_categories if category['id'] == category_id)

    # Display dropdowns for selecting state and category, and show problems based on the selections.
    state_id = st.selectbox(
        "Κατάτασταση:",
        options = list(state['id'] for state in all_states),
        format_func = lambda x: get_state_label(x))
    
    category_id = st.selectbox(
        "Κατηγορία:",
        options = list(category['id'] for category in all_categories),
        format_func = lambda x: get_category_label(x))

    show_problems(state_id, category_id)