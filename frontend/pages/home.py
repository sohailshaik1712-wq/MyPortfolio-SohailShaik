from datetime import datetime

import streamlit as st
from PIL import Image

experiences = [
    {
        "role": "System Engineer — Data Platform / MDM Engineer",
        "company": "Tata Consultancy Services (Client: Diageo)",
        "start": "2024-06",
        "end": None,  # Present
        "details": [
            "Engineered scalable data pipelines and automated workflows using modular programming principles.",
            "Built REST API integrations and backend services in Java/JS used across enterprise systems.",
            "Applied algorithmic business rules for validation, transformation, and enrichment of large datasets.",
            "Worked in Agile teams collaborating with cross-functional engineers to deliver high-quality solutions.",
        ],
    },
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
    initial_sidebar_state="collapsed",
)

# ----------------------------
# Global Styling
# ----------------------------
st.markdown(
    """
    <style>
    /* Main container alignment */
    .main {
        padding-top: 2rem;
    }

    /* 1. FORCE COLUMN CENTERING */
    /* This ensures everything inside the left column stays on the center axis */
    [data-testid="column"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    /* 2. PROFILE IMAGE - CIRCULAR & CENTERED */
    .profile-img img {
        border-radius: 50% !important;
        border: 4px solid #38bdf8;
        width: 180px !important;
        height: 180px !important;
        object-fit: cover;
        aspect-ratio: 1 / 1; /* Guaranteed circle */
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        margin-bottom: 1.5rem;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* 3. BUTTONS - UNIFIED WIDTH & CENTERING */
    .stButton, .stDownloadButton, .stLinkButton {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
    }


    /* Update this section in your existing <style> block */
    .stButton button,
    .stDownloadButton button,
    .stLinkButton a {
        width: 150px !important; /* Changed from 220px to fill the column */
        max-width: 150px !important;
        min-width: 150px !important;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.85rem; /* Slightly smaller text to ensure it fits on one line */
        transition: all 0.2s ease;
    }

    /* 4. TEXT ALIGNMENT */
    /* Forces the name and caption to use the full width for centering */
    .stMarkdown div {
        width: 100%;
    }

    /* Header styling */
    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #f8fafc;
    }

    /* Skill and Project Cards */
    .skill-card, .project-card {
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #1e293b;
        background: #020617;
        text-align: center;
    }

    .skill-card h4 {
        margin-bottom: 0.5rem;
        color: #38bdf8;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Layout
# ----------------------------
left, right = st.columns([1, 2.75], gap="large")

# =====================================================
# LEFT PANEL (VERTICAL ALIGNMENT OPTIMIZED)
# =====================================================
with left:
    # 1. Profile Image with explicit centering wrapper
    try:
        import base64
        from io import BytesIO

        img = Image.open("assets/sohail_photo.jpeg")
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        # We use 'text-align: center' on the outer div to snap the image to the middle
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; width: 100%;">
                <div class="profile-img">
                    <img src="data:image/jpeg;base64,{img_str}">
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    except FileNotFoundError:
        st.markdown(
            '<div class="profile-img" style="margin:auto;">📷</div>',
            unsafe_allow_html=True,
        )

    # 2. Name & Caption (Using HTML to ensure identical center-point)
    st.markdown(
        """
        <div style="text-align: center; width: 100%;">
            <h2 style="margin-left: 1.5rem; margin-bottom: 0; white-space: nowrap;">Sohail Shaik</h2>
            <p style="color: #94a3b8; margin-top: 0; font-size: 0.9rem;">MDM / Data Integration Engineer</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)
    st.divider()

    # =====================================================
    # 3. Standardized Action Buttons (Two-Column Layout)
    # =====================================================
    # Create two equal-width sub-columns
    btn_col1, btn_col2 = st.columns([1, 1], gap="medium")

    with btn_col1:
        st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/sohailshaik1107/")
        st.link_button("💡 LeetCode", "https://leetcode.com/u/shaiksohail_1107/")

    with btn_col2:
        st.link_button("🌐 GitHub", "https://github.com/sohailshaik1712-wq")

        # Resume Download logic in the second column
        try:
            with open("assets/Sohail-Shaik-Resume.pdf", "rb") as f:
                st.download_button(
                    "📄 Resume",  # Shortened text to fit two columns better
                    f.read(),
                    file_name="Sohail-Shaik-Resume.pdf",
                    mime="application/pdf",
                )
        except FileNotFoundError:
            st.button("📄 Missing", disabled=True)


# =====================================================
# RIGHT PANEL
# =====================================================
with right:
    # Hero Section
    st.title("Hey, I'm Sohail 👋")

    st.markdown(
        """
        ### MDM / Data Platform Engineer @ TCS | MLOps Enthusiast

        📍 Hyderabad, India
        """
    )

    st.write(
        """
        I’m a System Engineer at Tata Consultancy Services, specializing in the Data Platform and MDM (Master Data Management) space. Currently, I work as a Data Platform Engineer for Diageo, where I design governed, analytics-ready pipelines that turn enterprise data into reliable, decision-ready assets.
        I operate at the intersection of Data Governance and Automation, making sure large-scale datasets don’t just move fast, but move right.
        """
    )

    st.write("""
        Outside office hours, I don’t just code—I architect. I build and experiment with multiple cloud-native applications that serve as testing grounds for CI/CD pipelines, FastAPI performance, and Cloud Run scalability. These systems are where I validate ideas, push limits, and apply the same engineering discipline I use on enterprise platforms.
        Alongside this, I actively pursue Data Structures and Algorithms as a long-term craft—solving problems, refining patterns, and strengthening the fundamentals that power everything I build. For me, clean systems start with clear thinking.
        """)

    # Metrics
    m1, m2, m3 = st.columns(3)

    m1.metric("Experience", calculate_total_experience(experiences))
    m2.metric("Education", "8.42 CGPA")
    m3.metric("Primary Focus", "MLOps")


# =====================================================
# Skills
# =====================================================
st.divider()
st.markdown('<div class="section-title">🛠️ Tech Stack</div>', unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown(
        """
        <div class="skill-card">
        <h4>Languages</h4>
        <p>Python • Java • JS • SQL</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with s2:
    st.markdown(
        """
        <div class="skill-card">
        <h4>Databases</h4>
        <p>Postgres • MySQL • SQLite</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with s3:
    st.markdown(
        """
        <div class="skill-card">
        <h4>Frameworks</h4>
        <p>FastAPI • Django • Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with s4:
    st.markdown(
        """
        <div class="skill-card">
        <h4>DevOps</h4>
        <p>Docker • Git • Kafka • CI/CD</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# =====================================================
# Experience
# =====================================================
st.markdown('<div class="section-title">💼 Experience</div>', unsafe_allow_html=True)

with st.expander(
    "System Engineer — Data Platform / MDM Engineer | Tata Consultancy Services",
    expanded=True,
):
    st.write("**June 2024 – Present** | Client: Diageo | Hyderabad, India")

    st.markdown(
        """
        - Engineered scalable data pipelines and automated workflows using modular programming principles
        - Built REST API integrations and backend services in Java/JS used across enterprise systems
        - Applied algorithmic business rules for validation, transformation, and enrichment of large datasets
        - Worked in Agile teams collaborating with cross-functional engineers to deliver high-quality solutions
        """
    )

st.divider()

# =====================================================
# Education
# =====================================================
st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Bachelor of Technology (B.Tech)**")
    st.caption("Electronics and Communication")
    st.caption("VNR Vignanajyothi Institute of Engineering & Technology")
    st.caption("CGPA: 8.42 | 2020 – 2024")

with col2:
    st.markdown("**Senior Secondary (XII)**")
    st.caption("Science")
    st.caption("Sri Chaitanya Educational Institutions")
    st.caption("GPA: 9.63 | 2018 – 2020")

with col3:
    st.markdown("**Secondary (X)**")
    st.caption("Science")
    st.caption("Vishwabharati English Medium High School, Gudivada")
    st.caption("GPA: 9.80 | 2017 – 2018")

st.divider()

# =====================================================
# Certifications
# =====================================================
st.markdown(
    '<div class="section-title">🏆 Certifications</div>', unsafe_allow_html=True
)

cert_col1, cert_col2 = st.columns(2)

with cert_col1:
    st.markdown("""
    - **[Machine Learning](https://www.coursera.org/account/accomplishments/specialization/UCX4VK7H22A4)** — Coursera | Stanford
    - **[Machine Learning with Python](https://courses.cognitiveclass.ai/certificates/2efd0f37d75846af83748dba280968da)** — IBM
    """)

with cert_col2:
    st.markdown("""
    - **[SQL for Data Science](https://www.coursera.org/account/accomplishments/verify/FVK729TNTPHU)** — IBM
    - **[Data Analysis with Python](https://www.coursera.org/account/accomplishments/verify/9Z7YBZ8H7GXA)** — IBM
    """)

st.divider()

# =====================================================
# Projects Navigation
# =====================================================

st.markdown('<div class="project-nav-container">', unsafe_allow_html=True)
st.write("### 🚀 Ready to see my work?")
st.write(
    "Explore my projects and If you want to contact me you can feel free to email me here."
)
if st.button("View Projects →"):
    st.switch_page("pages/projects.py")
st.link_button("📧 Email", "mailto:sohailshaik1712@gmail.com")
st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------
# Footer
# ----------------------------
st.divider()

st.caption(
    "© 2026 Sohail Shaik • Built with Streamlit, FastAPI & Google Cloud • Data Platform Engineer @ TCS"
)
