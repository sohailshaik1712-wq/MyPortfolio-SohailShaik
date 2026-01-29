import streamlit as st

# 1. Global Page Config (Only call this ONCE)
st.set_page_config(
    page_title="Sohail Shaik | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Define the pages
home_page = st.Page("pages/home.py", title="Home", icon=":material/home:", default=True)
projects_page = st.Page("pages/projects.py", title="Projects", icon=":material/work:")
login_page = st.Page(
    "pages/admin_login.py", title="Admin Login", icon=":material/login:"
)
panel_page = st.Page(
    "pages/admin_panel.py", title="Admin Panel", icon=":material/dashboard:"
)

# 3. Session Logic
if "token" not in st.session_state:
    st.session_state.token = None

# 4. Create Navigation with Horizontal Bar
# Use position="top" to move the menu from the side to the top
if st.session_state.token:
    pg = st.navigation(
        {"Portfolio": [home_page, projects_page, panel_page]}, position="top"
    )
else:
    pg = st.navigation(
        {"Portfolio": [home_page, projects_page, login_page]}, position="top"
    )

# 5. Run the Navigation
pg.run()

# 6. Logout Logic (Moves to sidebar ONLY when logged in)
if st.session_state.token:
    with st.sidebar:
        if st.button("Logout"):
            st.session_state.token = None
            st.rerun()
