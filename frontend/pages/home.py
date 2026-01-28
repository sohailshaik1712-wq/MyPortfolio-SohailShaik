import streamlit as st
from PIL import Image

# 1. Advanced CSS for Precision Alignment
st.markdown(
    """
    <style>
        /* 1. Eliminate the gap between elements in the sidebar column */
        [data-testid="column"]:nth-of-type(1) [data-testid="stVerticalBlock"] {
            gap: 0.5rem !important;
            align-items: center;
            display: flex;
            flex-direction: column;
        }

        /* 2. Precision Circular Image */
        [data-testid="stImage"] img {
            border-radius: 50%;
            border: 5px solid #38bdf8;
            object-fit: cover;
            aspect-ratio: 1 / 1;
            width: 200px;
            height: 200px;
            margin-bottom: 10px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }

        /* 3. Unified Button Styling */
        .stButton, .stDownloadButton, .stLinkButton {
            width: 100% !important;
            display: flex;
            justify-content: center;
        }

        .stButton button, .stDownloadButton button, .stLinkButton a {
            width: 200px !important; /* Perfectly matches image width */
            border-radius: 10px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
        }

        /* Hover effect for a "Pro" feel */
        .stButton button:hover {
            border-color: #38bdf8 !important;
            color: #38bdf8 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 2. Main Layout
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    try:
        img = Image.open("assets/sohail_photo.jpeg")
        st.image(img)
    except FileNotFoundError:
        st.info("📷 Photo Missing")

    # Action Buttons (Centered & Aligned)
    st.link_button("📧 Email Me", "mailto:sohailshaik1712@gmail.com")
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/sohailshaik1107/")

    try:
        with open("assets/Sohail-Shaik-Resume.pdf", "rb") as f:
            st.download_button(
                label="📄 Download Resume",
                data=f.read(),
                file_name="Sohail-Shaik-Resume.pdf",
                mime="application/pdf",
            )
    except FileNotFoundError:
        st.caption("Resume PDF not found.")

with col2:
    st.title("Hey, I'm Sohail! 👋")
    st.write("### Data Platform Engineer | MLOps Hobbyist")
    st.caption("📍 Hyderabad, India | TCS System Engineer")

    st.write(
        """
        I’m a **System Engineer at TCS** who loves the "Ops" in MLOps.
        Professionally, I build heavy-duty data platforms for **Diageo**;
        by night, I obsess over CI/CD for Machine Learning.
        """
    )

    # Clean Badges
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Experience", "TCS/Diageo")
    with c2:
        st.metric("Education", "8.42 CGPA")
    with c3:
        st.metric("Focus", "MLOps")

st.divider()

# 3. Skills Grid
st.markdown("### 🛠️ My Toolkit")
s1, s2, s3 = st.columns(3)
with s1:
    with st.container(border=True):
        st.markdown("**Core Stack**")
        st.caption("Python, Java, SQL, FastAPI")
with s2:
    with st.container(border=True):
        st.markdown("**MLOps**")
        st.caption("Docker, Kafka, CI/CD, Git")
with s3:
    with st.container(border=True):
        st.markdown("**Databases**")
        st.caption("Postgres, Neon, MySQL")

st.divider()

# 4. Experience & Projects
st.markdown("### 💼 Experience")
with st.expander("System Engineer @ Tata Consultancy Services", expanded=True):
    st.write("06/2024 - Present")
    st.write("- Engineered scalable pipelines for global product master data.")
    st.write("- Built Java/JS REST APIs for secure enterprise data delivery.")

st.markdown("### 🚀 Passion Projects")
h1, h2 = st.columns(2)
with h1:
    with st.container(border=True):
        st.markdown("**🧠 Alzheimer's Detection**")
        st.write("99.23% accuracy using EfficientNet B0-B6.")
with h2:
    with st.container(border=True):
        st.markdown("**🎬 Movie Recommender**")
        st.write("Personalized engine for 26M+ ratings.")
