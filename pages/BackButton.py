import streamlit as st


def show_back_button():
    st.markdown(
        """
<style>
    .back-button-fixed {
        position: fixed;
        top: 0.85rem;
        left: 0.85rem;
        z-index: 999999;
        background: white;
        border: 1px solid #d1d5db;
        border-radius: 6px;
        color: #111827;
        display: inline-block;
        font-size: 0.95rem;
        font-weight: 500;
        padding: 0.4rem 0.7rem;
        text-decoration: none;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    }

    .back-button-fixed:hover {
        background: #f9fafb;
        border-color: #9ca3af;
        color: #111827;
        text-decoration: none;
    }
</style>
<a class="back-button-fixed" href="http://localhost:8501/" target="_self">← Επιστροφή</a>
""",
        unsafe_allow_html=True,
    )
