from datetime import datetime

import streamlit as st
from PIL import Image

experiences = [
    {
        "role": "System Engineer",
        "company": "TCS",
        "start": "2024-06",
        "end": None,  # Present
        "details": [],
    },
    # Add future roles here
]


def calculate_total_experience(experiences):
    total_months = 0
    now = datetime.now()

    for exp in experiences:
        start = datetime.strptime(exp["start"], "%Y-%m")

        end = datetime.strptime(exp["end"], "%Y-%m") if exp["end"] else now

        months = (end.year - start.year) * 12 + (end.month - start.month)

        total_months += max(months, 0)

    years = total_months // 12
    rem = total_months % 12

    if years and rem:
        return f"{years}.{rem // 2}+ Years"
    elif years:
        return f"{years}+ Years"
    else:
        return f"{rem} Months"


# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Sohail Shaik | Portfolio",
    page_icon="👨‍💻",
    layout="wide",
)

# ----------------------------
# Global Styling
# ----------------------------
st.markdown(
    """
    <style>

    /* Main container */
    .main {
        padding-top: 2rem;
    }

    /* Profile image */
    .profile-img img {
        border-radius: 50%;
        border: 4px solid #38bdf8;
        width: 180px;
        height: 180px;
        object-fit: cover;
        box-shadow: 0 6px 12px rgba(0,0,0,0.12);
        margin-bottom: 1rem;
    }

    /* Sidebar card */
    .profile-card {
        background: #0f172a;
        padding: 2rem 1.5rem;
        border-radius: 14px;
        text-align: center;
        border: 1px solid #1e293b;
    }

    .stButton,
    .stDownloadButton,
    .stLinkButton {
        display: flex !important;
        justify-content: center !important;
    }

    .stButton button,
    .stDownloadButton button,
    .stLinkButton a {
        width: 220px !important;   /* <-- ONE fixed width */
        max-width: 220px !important;
        min-width: 220px !important;

        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton button:hover {
        border-color: #38bdf8;
        color: #38bdf8;
    }

    /* Section headers */
    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    /* Skill cards */
    .skill-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #1e293b;
        background: #020617;
        text-align: center;
    }

    /* Project cards */
    .project-card {
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #1e293b;
        background: #020617;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Layout
# ----------------------------
left, right = st.columns([1, 2.5], gap="large")

# =====================================================
# LEFT PANEL
# =====================================================
with left:
    # st.markdown('<div class="profile-card">', unsafe_allow_html=True)

    # Profile Image
    try:
        img = Image.open("assets/sohail_photo.jpeg")
        st.markdown('<div class="profile-img">', unsafe_allow_html=True)
        st.image(img)
        st.markdown("</div>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.info("📷 Profile photo missing")

    # Name
    st.markdown("## Sohail Shaik")
    st.caption("Data Platform Engineer | MLOps")

    st.divider()

    # Links
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/sohailshaik1107/")
    st.link_button("🌐 GitHib", "https://github.com/sohailshaik1712-wq")
    st.link_button("📧 Email", "mailto:sohailshaik1712@gmail.com")

    # Resume
    try:
        with open("assets/Sohail-Shaik-Resume.pdf", "rb") as f:
            st.download_button(
                "📄 Download Resume",
                f.read(),
                file_name="Sohail-Shaik-Resume.pdf",
                mime="application/pdf",
            )
    except FileNotFoundError:
        st.caption("Resume not found")

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================
# RIGHT PANEL
# =====================================================
with right:
    # Hero Section
    st.title("Hey, I'm Sohail 👋")

    st.markdown(
        """
        ### Data Platform Engineer @ TCS | MLOps Enthusiast

        📍 Hyderabad, India
        """
    )

    st.write(
        """
        I’m a **System Engineer at Tata Consultancy Services** working on
        enterprise-grade data platforms for **Diageo**.

        Outside work, I specialize in **MLOps, CI/CD, and scalable ML systems** —
        turning models into reliable production services.
        """
    )

    # Metrics
    m1, m2, m3 = st.columns(3)

    m1.metric("Experience", calculate_total_experience(experiences))
    m2.metric("Education", "8.42 CGPA")
    m3.metric("Primary Focus", "MLOps")

    st.divider()

    # =====================================================
    # Skills
    # =====================================================
    st.markdown('<div class="section-title">🛠️ Tech Stack</div>', unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)

    with s1:
        st.markdown(
            """
            <div class="skill-card">
            <h4>Core</h4>
            <p>Python • Java • SQL • FastAPI</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with s2:
        st.markdown(
            """
            <div class="skill-card">
            <h4>MLOps</h4>
            <p>Docker • Kafka • CI/CD • Git</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with s3:
        st.markdown(
            """
            <div class="skill-card">
            <h4>Databases</h4>
            <p>Postgres • Neon • MySQL</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # =====================================================
    # Experience
    # =====================================================
    st.markdown(
        '<div class="section-title">💼 Experience</div>', unsafe_allow_html=True
    )

    with st.expander("System Engineer — Tata Consultancy Services", expanded=True):
        st.write("**June 2024 – Present**")

        st.markdown(
            """
            - Designed scalable ETL pipelines for product master data
            - Built secure Java & JS REST APIs
            - Optimized data delivery for global teams
            - Integrated CI/CD for analytics workloads
            """
        )

    st.divider()

    # =====================================================
    # Projects
    # =====================================================

    st.markdown('<div class="project-nav-container">', unsafe_allow_html=True)
    st.write("### Ready to see my work?")
    if st.button("🚀 View My Projects"):
        st.switch_page("pages/projects.py")
    st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------
# Footer
# ----------------------------
st.divider()

st.caption("© 2026 Sohail Shaik • Built with Streamlit, FastAPI & Google Cloud")
