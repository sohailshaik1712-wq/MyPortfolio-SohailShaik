import streamlit as st
from services.api import get_projects

st.set_page_config(page_title="Projects | Sohail Shaik", layout="wide")

st.title("📂 Project Gallery")
st.write("A collection of my work in Data Engineering, MLOps, and Deep Learning.")

res = get_projects()

if res.status_code == 200:
    all_projects = res.json()

    # --- 1. SEARCH & FILTER UI ---
    search_col, filter_col = st.columns([2, 1])

    with search_col:
        search_query = st.text_input(
            "🔍 Search projects by title or tech stack...",
            placeholder="e.g. Docker, EfficientNet, Java",
        )

    with filter_col:
        # Extract unique categories from tech_stack or metadata if available
        # For now, let's use common tags found in your toolkit
        categories = ["All", "MLOps", "Deep Learning", "Data Engineering", "Backend"]
        selected_category = st.selectbox("📂 Filter by Category", categories)

    # --- 2. FILTERING LOGIC ---
    filtered_projects = []
    for p in all_projects:
        # Match search query
        match_search = (
            search_query.lower() in p["title"].lower()
            or search_query.lower() in p.get("tech_stack", "").lower()
            or search_query.lower() in p["description"].lower()
        )

        # Match category (checks if category name exists in tech_stack or title)
        match_category = (
            selected_category == "All"
            or selected_category.lower() in p.get("tech_stack", "").lower()
            or selected_category.lower() in p["title"].lower()
        )

        if match_search and match_category:
            filtered_projects.append(p)

    st.divider()

    # --- 3. RENDER FILTERED GRID ---
    if not filtered_projects:
        st.info("No projects found matching those criteria. Try a different keyword!")
    else:
        # 2-Column Grid
        cols = st.columns(2)
        for idx, p in enumerate(filtered_projects):
            with cols[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### 🛠️ {p['title']}")

                    # Tech Badges
                    tech_list = p.get("tech_stack", "").split(",")
                    badges = "".join(
                        [
                            f'<code style="color: #38bdf8; background: #1e293b; padding: 2px 6px; border-radius: 4px; margin-right: 5px; font-size: 0.8rem;">{t.strip()}</code>'
                            for t in tech_list
                            if t.strip()
                        ]
                    )
                    st.markdown(badges, unsafe_allow_html=True)

                    st.write(f"\n{p['description']}")

                    # Action Buttons
                    b1, b2 = st.columns(2)
                    if p.get("github_url"):
                        b1.link_button(
                            "Code", p["github_url"], use_container_width=True
                        )
                    if p.get("live_url"):
                        b2.link_button(
                            "Demo",
                            p["live_url"],
                            use_container_width=True,
                            type="primary",
                        )
else:
    st.error(
        "Failed to fetch projects from the backend. Please check if the API is running."
    )
