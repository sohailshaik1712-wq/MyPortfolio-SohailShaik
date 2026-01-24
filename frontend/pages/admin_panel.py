import streamlit as st
from components.auth import is_logged_in
from services.api import create_project, delete_project, get_projects, update_project

st.set_page_config(page_title="Admin Panel | Sohail Shaik", layout="wide")

if not is_logged_in():
    st.warning("Login required")
    st.stop()

st.title("🛡️ Admin Dashboard")

# Create Tabs for different operations
tab1, tab2, tab3 = st.tabs(["➕ Create", "📝 Update", "🗑️ Delete"])

# Fetch latest projects for Update/Delete tabs
res = get_projects()
projects = res.json() if res.status_code == 200 else []

# --- TAB 1: CREATE ---
with tab1:
    st.subheader("Add New Project")
    with st.form("create_form", clear_on_submit=True):
        title = st.text_input("Title")
        desc = st.text_area("Description")
        tech = st.text_input("Tech Stack (comma separated)")
        git = st.text_input("GitHub URL")
        live = st.text_input("Live URL")

        if st.form_submit_button("Add Project"):
            payload = {
                "title": title,
                "description": desc,
                "tech_stack": tech,
                "github_url": git,
                "live_url": live,
            }
            response = create_project(payload, st.session_state.token)
            if response.status_code == 200:
                st.success(f"Project '{title}' created!")
                st.rerun()
            else:
                st.error("Error creating project")

# --- TAB 2: UPDATE ---
with tab2:
    st.subheader("Modify Existing Project")
    if not projects:
        st.info("No projects found to update.")
    else:
        project_to_edit = st.selectbox(
            "Select Project",
            options=projects,
            format_func=lambda x: x["title"],
            key="update_select",
        )

        # GUARD CLAUSE: Only proceed if a project is actually selected
        if project_to_edit is not None:
            with st.form("update_form"):
                u_title = st.text_input("Title", value=project_to_edit["title"])
                u_desc = st.text_area(
                    "Description", value=project_to_edit["description"]
                )
                u_tech = st.text_input(
                    "Tech Stack", value=project_to_edit.get("tech_stack", "")
                )
                u_git = st.text_input(
                    "GitHub URL", value=project_to_edit.get("github_url", "")
                )
                u_live = st.text_input(
                    "Live URL", value=project_to_edit.get("live_url", "")
                )

                if st.form_submit_button("Save Changes"):
                    updated_payload = {
                        "title": u_title,
                        "description": u_desc,
                        "tech_stack": u_tech,
                        "github_url": u_git,
                        "live_url": u_live,
                    }
                    response = update_project(
                        project_to_edit["id"], updated_payload, st.session_state.token
                    )
                    if response.status_code == 200:
                        st.success("Project updated!")
                        st.rerun()
        else:
            st.warning("Please select a project to edit.")

# --- TAB 3: DELETE ---
with tab3:
    st.subheader("Remove Project")
    if not projects:
        st.info("No projects found.")
    else:
        project_to_del = st.selectbox(
            "Select Project to Delete",
            options=projects,
            format_func=lambda x: x["title"],
            key="delete_select",
        )

        # GUARD CLAUSE: Only proceed if a project is selected to avoid subscript error
        if project_to_del is not None:
            st.warning(f"Are you sure you want to delete '{project_to_del['title']}'?")
            if st.button("Confirm Delete", type="primary"):
                response = delete_project(project_to_del["id"], st.session_state.token)
                if response.status_code == 200:
                    st.success("Project deleted.")
                    st.rerun()
                else:
                    st.error("Failed to delete project.")
        else:
            st.warning("Please select a project to delete.")
