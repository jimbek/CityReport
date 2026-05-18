import streamlit as st

view_page = st.Page("pages/view.py", title="Προεπισκόπηση",icon=":material/search:")
statistics_page = st.Page("pages/statistics.py", title="Στατιστικά",icon=":material/bar_chart:")

edit_page = st.Page("pages/edit.py", title="Επεξεργασία",icon=":material/edit:", visibility = "hidden")
comment_page = st.Page("pages/comments.py", title="Σχόλια",icon=":material/chat:", visibility = "hidden")

pg = st.navigation([view_page, statistics_page, edit_page, comment_page])
pg.run()