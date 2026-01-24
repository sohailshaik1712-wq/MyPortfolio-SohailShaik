import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 1. Define the pages
# These paths must match your 'pages' folder exactly
home_page = st.Page("pages/home.py", title="Home", icon=":material/home:", default=True)
projects_page = st.Page("pages/projects.py", title="Projects", icon=":material/work:")
login_page = st.Page(
    "pages/admin_login.py", title="Admin Login", icon=":material/login:"
)
panel_page = st.Page(
    "pages/admin_panel.py", title="Admin Panel", icon=":material/dashboard:"
)

# 2. Session Logic
if "token" not in st.session_state:
    st.session_state.token = None

# 3. Create Navigation Structure
if st.session_state.token:
    # Pages shown when logged in
    pg = st.navigation({"Portfolio": [home_page, projects_page, panel_page]})
else:
    # Pages shown when logged out
    pg = st.navigation({"Portfolio": [home_page, projects_page, login_page]})

# 4. Global Styling (Optional)
st.set_page_config(page_title="Sohail Shaik | Portfolio", layout="wide")

# 5. Run the Navigation
pg.run()

# 6. Add Logout Button (Optional: stays at bottom of sidebar)
if st.session_state.token:
    if st.sidebar.button("Logout"):
        st.session_state.token = None
        st.rerun()
