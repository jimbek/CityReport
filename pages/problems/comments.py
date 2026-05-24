# This pages allows admins to add comments on problems.
import html

import streamlit as st

from pages.BackButton import show_back_button
from lib.repos.CommentsRepository import CommentsRepository
from lib.repos.ProblemsRepository import ProblemsRepository
from services.EmailService import EmailService

show_back_button()

comments_repo = CommentsRepository()
problems_repo = ProblemsRepository()
email_service = EmailService()

st.markdown(
    """
<style>
    .comment-box {
        border-left: 3px solid #d1d5db;
        margin-bottom: 0.5rem;
        padding: 0.25rem 0 0.25rem 0.75rem;
    }

    .comment-author {
        color: #4b5563;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 0.1rem;
    }

    .comment-content {
        color: #111827;
        font-size: 1rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

problem_id = st.query_params.get('problemId', st.session_state.get("selected_problem_id", ""))
st.session_state["selected_problem_id"] = problem_id

problem = problems_repo.get_problem_by_id(problem_id)
comments = comments_repo.get_comments(problem_id)

if problem is None:
    st.error("Το πρόβλημα δεν βρέθηκε.")
    st.stop()

reported_email = problem.get("reportedByEmail")

comment_status = st.session_state.pop("comment_status", None)

if comment_status:
    st.success(comment_status)

# Display chat messages from history on app rerun.
for comment in comments:
    author = html.escape(comment["author"])
    content = html.escape(comment["content"])

    st.markdown(
        f"""
<div class="comment-box">
    <div class="comment-author">{author}</div>
    <div class="comment-content">{content}</div>
</div>
""",
        unsafe_allow_html=True,
    )

with st.form("comment_form", clear_on_submit=True):
    prompt = st.text_area("Πληκτρολογήστε το σχόλιό σας εδώ...")

    send_email = st.checkbox(
        "Αποστολή email στον πολίτη όταν προστεθεί σχόλιο",
        value=False,
        disabled=not bool(reported_email))

    if reported_email:
        st.caption(f"Το email θα σταλεί στο: {reported_email}")
    else:
        st.error("Το συγκεκριμένο πρόβλημα δεν έχει email πολίτη, οπότε δεν μπορεί να σταλεί email.")

    submit_comment = st.form_submit_button(label="Προσθήκη σχολίου", icon=":material/send:")

    if submit_comment:
        if not prompt:
            st.warning("Πληκτρολογήστε ένα σχόλιο πριν το αποθηκεύσετε.")
        else:
            comments_repo.add_comment({
                "problemId": problem_id,
                "author": "Admin",
                "content": prompt
            })

            if send_email:
                email_sent, email_message = email_service.send_email(reported_email, problem["title"], prompt)

                if email_sent:
                    st.success(email_message)
                else:
                    st.error(email_message)

            st.session_state["comment_status"] = "Το σχόλιο προστέθηκε."
            st.rerun()
