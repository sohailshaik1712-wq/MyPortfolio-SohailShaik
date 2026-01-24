import streamlit as st
from services.api import get_projects

st.title("📂 Project Gallery")

res = get_projects()
if res.status_code == 200:
    projects = res.json()

    # 2-Column Grid
    cols = st.columns(2)
    for idx, p in enumerate(projects):
        # Alternate between column 0 and 1
        with cols[idx % 2]:
            with st.container(border=True):
                # Title with an icon
                st.markdown(f"### 🛠️ {p['title']}")

                # Tech Badges (Horizontal)
                tech_list = p.get("tech_stack", "").split(",")
                badges = "".join(
                    [
                        f'<code style="color: #38bdf8; background: #1e293b; padding: 2px 6px; border-radius: 4px; margin-right: 5px;">{t.strip()}</code>'
                        for t in tech_list
                    ]
                )
                st.markdown(badges, unsafe_allow_html=True)

                st.write(f"\n{p['description']}")

                # Action Buttons
                b1, b2 = st.columns(2)
                if p.get("github_url"):
                    b1.link_button("Code", p["github_url"], use_container_width=True)
                if p.get("live_url"):
                    b2.link_button(
                        "Demo", p["live_url"], use_container_width=True, type="primary"
                    )
