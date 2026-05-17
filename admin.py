import streamlit as st

search_page = st.Page("pages/search.py", title="Αναζήτηση προβλημάτων",icon=":material/search:")
statistics_page = st.Page("pages/statistics.py", title="Στατιστικά",icon=":material/bar_chart:")

pg = st.navigation([search_page, statistics_page])
pg.run()