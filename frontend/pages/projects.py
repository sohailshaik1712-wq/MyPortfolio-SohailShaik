import streamlit as st
from services.api import get_projects

st.set_page_config(page_title="Projects | Sohail Shaik", layout="wide")

st.title("📂 Project Gallery")
st.write("A collection of my work in Data Engineering, MLOps, and Deep Learning.")

# --- FETCH PROJECTS WITH LOADING STATE ---
with st.spinner("Loading projects..."):
    try:
        res = get_projects()
    except Exception as e:
        st.error(f"❌ Failed to connect to backend API: {str(e)}")
        st.stop()

if res.status_code == 200:
    all_projects = res.json()

    if not all_projects:
        st.info("No projects found. Add some projects to display them here!")
        st.stop()

    # --- 1. SEARCH, FILTER & SORT UI ---
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        # Real-time search
        search_query = st.text_input(
            "🔍 Search projects by title, description, or tech stack...",
            placeholder="e.g. Docker, EfficientNet, Java",
            key="search_box",
        )

    with col2:
        # Category filter
        categories = [
            "All",
            "MLOps",
            "Deep Learning",
            "Data Engineering",
            "Backend",
            "Frontend",
        ]
        selected_category = st.selectbox(
            "📂 Category", categories, key="category_filter"
        )

    with col3:
        # Sort options
        sort_options = {
            "Newest First": "newest",
            "Oldest First": "oldest",
            "A → Z": "a-z",
            "Z → A": "z-a",
        }
        selected_sort = st.selectbox(
            "🔄 Sort By", list(sort_options.keys()), key="sort_by"
        )

    # --- 2. REAL-TIME FILTERING LOGIC ---
    def matches_search(project, query):
        """Check if project matches search query (partial matching)"""
        if not query:
            return True

        query_lower = query.lower().strip()

        # Split query into words for better matching (like Google)
        query_words = query_lower.split()

        # Combine all searchable text
        searchable_text = " ".join(
            [
                project.get("title", ""),
                project.get("description", ""),
                project.get("tech_stack", ""),
            ]
        ).lower()

        # Check if ALL query words appear in the searchable text (AND logic)
        return all(word in searchable_text for word in query_words)

    def matches_category(project, category):
        """Check if project matches selected category"""
        if category == "All":
            return True

        category_lower = category.lower()
        tech_stack_lower = project.get("tech_stack", "").lower()
        title_lower = project.get("title", "").lower()

        return category_lower in tech_stack_lower or category_lower in title_lower

    # Apply filters
    filtered_projects = [
        p
        for p in all_projects
        if matches_search(p, search_query) and matches_category(p, selected_category)
    ]

    # --- 3. SORTING LOGIC ---
    def sort_projects(projects, sort_type):
        """Sort projects based on selected option"""
        if sort_type == "newest":
            # Sort by created_at or id (descending)
            return sorted(
                projects,
                key=lambda x: x.get("created_at", x.get("id", 0)),
                reverse=True,
            )
        elif sort_type == "oldest":
            # Sort by created_at or id (ascending)
            return sorted(projects, key=lambda x: x.get("created_at", x.get("id", 0)))
        elif sort_type == "a-z":
            # Sort by title alphabetically
            return sorted(projects, key=lambda x: x.get("title", "").lower())
        elif sort_type == "z-a":
            # Sort by title reverse alphabetically
            return sorted(
                projects, key=lambda x: x.get("title", "").lower(), reverse=True
            )
        return projects

    # Apply sorting
    sorted_projects = sort_projects(filtered_projects, sort_options[selected_sort])

    st.divider()

    # --- 4. RENDER FILTERED & SORTED GRID WITH HIGHLIGHTING ---
    if not sorted_projects:
        st.info(
            "🔍 No projects found matching those criteria. Try a different keyword!"
        )
    else:
        # Show count with search query highlight
        info_parts = []
        if search_query:
            info_parts.append(f"matching '**{search_query}**'")
        if selected_category != "All":
            info_parts.append(f"in category '**{selected_category}**'")

        if info_parts:
            st.success(
                f"Found **{len(sorted_projects)}** project(s) {' '.join(info_parts)} • Sorted by **{selected_sort}**"
            )
        else:
            st.success(
                f"Showing all **{len(sorted_projects)}** project(s) • Sorted by **{selected_sort}**"
            )

        # 2-Column Grid
        cols = st.columns(2)

        for idx, p in enumerate(sorted_projects):
            with cols[idx % 2]:
                with st.container(border=True):
                    st.markdown(f"### 🛠️ {p.get('title', 'Untitled Project')}")

                    # Tech Badges with highlighting
                    tech_stack = p.get("tech_stack", "")
                    if tech_stack:
                        tech_list = [
                            t.strip() for t in tech_stack.split(",") if t.strip()
                        ]

                        # Highlight matching tech tags
                        badges = []
                        for tech in tech_list:
                            # Check if this tech matches search query
                            is_match = (
                                search_query and search_query.lower() in tech.lower()
                            )

                            if is_match:
                                # Highlighted badge (yellow/gold)
                                badge = (
                                    f'<code style="color: #fbbf24; background: #1e293b; '
                                    f"padding: 2px 6px; border-radius: 4px; margin-right: 5px; "
                                    f'font-size: 0.8rem; border: 1px solid #fbbf24;">{tech}</code>'
                                )
                            else:
                                # Normal badge (blue)
                                badge = (
                                    f'<code style="color: #38bdf8; background: #1e293b; '
                                    f"padding: 2px 6px; border-radius: 4px; margin-right: 5px; "
                                    f'font-size: 0.8rem;">{tech}</code>'
                                )
                            badges.append(badge)

                        st.markdown("".join(badges), unsafe_allow_html=True)

                    # Description
                    description = p.get("description", "No description available.")
                    st.write(f"\n{description}")

                    # Optional: Show creation date if available
                    if p.get("created_at"):
                        st.caption(f"📅 Added: {p['created_at'][:10]}")

                    # Action Buttons
                    github_url = p.get("github_url")
                    live_url = p.get("live_url")

                    if github_url or live_url:
                        b1, b2 = st.columns(2)

                        if github_url:
                            b1.link_button(
                                "📂 Code", github_url, use_container_width=True
                            )

                        if live_url:
                            b2.link_button(
                                "🚀 Demo",
                                live_url,
                                use_container_width=True,
                                type="primary",
                            )

elif res.status_code == 404:
    st.warning("⚠️ No projects endpoint found. Please check your backend API.")

elif res.status_code == 500:
    st.error("❌ Backend server error. Please check the backend logs.")
    with st.expander("View Error Details"):
        st.code(res.text)

else:
    st.error(f"❌ Failed to fetch projects. Status code: {res.status_code}")
    with st.expander("View Error Details"):
        st.code(res.text)
