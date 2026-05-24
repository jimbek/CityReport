# Defines pages and navigation for the admin interface.
# Pages are defined in the pages/ directory and imported here.
import streamlit as st

from lib.repos.DatabaseInitializer import initialize_database

initialize_database()

index = st.Page("pages/index.py", title = "Προβλήματα", visibility = "hidden")

per_category = st.Page("pages/statistics/per_category.py", title = "Στατιστικά ανά κατηγορία",icon = ":material/bar_chart:")
per_state = st.Page("pages/statistics/per_state.py", title = "Στατιστικά ανά κατάσταση",icon = ":material/bar_chart:")

edit = st.Page("pages/problems/edit.py", title = "Επεξεργασία",icon = ":material/edit:", visibility = "hidden")
comment = st.Page("pages/problems/comments.py", title = "Σχόλια",icon = ":material/chat:", visibility = "hidden")

pg = st.navigation([index, per_category, per_state, edit, comment])
pg.run()
