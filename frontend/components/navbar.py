import streamlit as st


def show_navbar():
    # 1. THE FIX: This must run on every page to keep the default nav hidden
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 2. Your custom Sidebar content
    st.sidebar.title("Portfolio")
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/projects.py", label="Projects")

    if "token" in st.session_state and st.session_state.token:
        st.sidebar.page_link("pages/admin_panel.py", label="Admin Panel")
        if st.sidebar.button("Logout"):
            st.session_state.token = None
            st.rerun()
    else:
        st.sidebar.page_link("pages/admin_login.py", label="Admin Login")
