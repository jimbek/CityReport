# This pages allows admins to add comments on problems.
import datetime
import streamlit as st
import uuid

from lib.repos.CommentsRepository import CommentsRepository

comments_repo = CommentsRepository()
comments = comments_repo.get_comments(st.query_params.get('problemId', ['']))

# Display chat messages from history on app rerun.
for comment in comments:
    with st.chat_message(comment["author"]):
        st.markdown(comment["content"])

# React to user input
if prompt := st.chat_input("Πληκτρολογήστε το σχόλιό σας εδώ..."):
    
    # Save the comment to the repository.
    comments_repo.add_comment({
        "id": str(uuid.uuid4()),
        "problemId": st.query_params.get('problemId', ['']),
        "author": "Admin",
        "content": prompt,
        "createdAt": datetime.datetime.now().isoformat()
    })

    # TODO: Κάλεσε τη μέθοδο send_email της κλάσης EmailService.
    # TODO: Βάλε ως θέμα τον τίτλο του προβλήματος και ως περιεχόμενο το σχόλιο που μόλις προστέθηκε.

    # Display the user's message in the chat message container.
    st.chat_message("Admin").markdown(prompt)