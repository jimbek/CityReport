import datetime
import streamlit as st
import uuid

from lib.repos.CommentsRepository import CommentsRepository

comments_repo = CommentsRepository()
comments = comments_repo.get_comments(st.query_params.get('problemId', ['']))

# Display chat messages from history on app rerun
for comment in comments:
    with st.chat_message(comment["author"]):
        st.markdown(comment["content"])

# React to user input
if prompt := st.chat_input("Πληκτρολογήστε το σχόλιό σας εδώ..."):
    comments_repo.add_comment({
        "id": str(uuid.uuid4()),
        "problemId": st.query_params.get('problemId', ['']),
        "author": "Admin",
        "content": prompt,
        "createdAt": datetime.datetime.now().isoformat()
    })
    st.chat_message("Admin").markdown(prompt)