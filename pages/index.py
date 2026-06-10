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

st.markdown("<h1 style='font-size: 1.75rem;'>Προβλήματα</h1>", unsafe_allow_html=True)

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

# Function to display problems based on selected state, category, search text, and sorting option.
def format_date(date_text: str):
    if date_text is None:
        return ""

    return date_text.replace("T", " ")[:16]


def show_problems(stateId: str, categoryId: str, sortBy: str, searchText: str):
    global container
    
    problems = problems_repo.get_all_problems(categoryId, stateId, sortBy, searchText)

    if not problems:
        container.write("Δεν βρέθηκαν προβλήματα με τα επιλεγμένα κριτήρια.")
        return

    header = container.columns([2, 3, 1, 1, 1.4, 1.4, 1])
    header[0].markdown("**Τίτλος**")
    header[1].markdown("**Περιγραφή**")
    header[2].markdown("**Μήκος**")
    header[3].markdown("**Πλάτος**")
    header[4].markdown("**Καταχώρηση**")
    header[5].markdown("**Ενημέρωση**")
    header[6].markdown("**Ενέργειες**")

    for problem in problems:
        row = container.columns([2, 3, 1, 1, 1.4, 1.4, 1])
        row[0].write(problem['title'])
        row[1].write(problem['description'])
        row[2].write(problem['longitude'])
        row[3].write(problem['latitude'])
        row[4].write(format_date(problem['createdAt']))
        row[5].write(format_date(problem['updatedAt']))

        action_buttons = row[6].columns(2)

        action_buttons[0].page_link(
            "pages/problems/edit.py",
            label = "",
            icon = ":material/edit:",
            query_params = {"problemId": problem['id']})

        action_buttons[1].page_link(
            "pages/problems/comments.py",
            label = "",
            icon = ":material/chat:",
            query_params = {"problemId": problem['id']})

# Display sidebar options for filtering problems by state and category.
with st.sidebar:
    st.subheader("Επιλογές")

    def clear_search():
        st.session_state["problem_search_text"] = ""

    # Helper function to get the label for a given state ID.
    def get_state_label(state_id):
        return next(state['label'] for state in all_states if state['id'] == state_id)
    
    # Helper function to get the label for a given category ID.
    def get_category_label(category_id):
        return next(category['label'] for category in all_categories if category['id'] == category_id)

    # Display text search, dropdown filters, and sorting controls.
    search_text = st.text_input(
        "Αναζήτηση:",
        placeholder = "Γράψτε λέξη από τίτλο ή περιγραφή",
        key = "problem_search_text")

    st.button("Καθαρισμός αναζήτησης", on_click = clear_search)

    state_id = st.selectbox(
        "Κατάσταση:",
        options = list(state['id'] for state in all_states),
        format_func = lambda x: get_state_label(x))
    
    category_id = st.selectbox(
        "Κατηγορία:",
        options = list(category['id'] for category in all_categories),
        format_func = lambda x: get_category_label(x))

    sort_options = {
        "Χωρίς ταξινόμηση": "",
        "Ημερομηνία καταχώρησης": "createdAt",
        "Ημερομηνία τελευταίας ενημέρωσης": "updatedAt",
    }

    sort_label = st.selectbox("Ταξινόμηση:", options = list(sort_options.keys()))

    show_problems(state_id, category_id, sort_options[sort_label], search_text)
