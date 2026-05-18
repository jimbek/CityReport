import streamlit as st

view_page = st.Page("pages/view.py", title="Προεπισκόπηση",icon=":material/search:")
edit_page = st.Page("pages/edit.py", title="Επεξεργασία",icon=":material/edit:", visibility = "hidden")
statistics_page = st.Page("pages/statistics.py", title="Στατιστικά",icon=":material/bar_chart:")

pg = st.navigation([view_page, edit_page, statistics_page])
pg.run()