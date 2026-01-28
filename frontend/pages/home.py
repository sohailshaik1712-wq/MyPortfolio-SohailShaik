import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Sohail Shaik | Data Platform Engineer", page_icon="💼", layout="wide"
)

# Advanced CSS for Professional Look
st.markdown(
    """
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* Global Styling */
        * {
            font-family: 'Inter', sans-serif;
        }

        /* Remove default padding */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }

        /* Sidebar Column Alignment */
        [data-testid="column"]:nth-of-type(1) [data-testid="stVerticalBlock"] {
            gap: 1rem !important;
            align-items: center;
            display: flex;
            flex-direction: column;
        }

        /* Professional Circular Image with Gradient Border */
        [data-testid="stImage"] img {
            border-radius: 50%;
            border: none;
            object-fit: cover;
            aspect-ratio: 1 / 1;
            width: 220px;
            height: 220px;
            margin-bottom: 15px;
            box-shadow: 0 10px 25px rgba(56, 189, 248, 0.3);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 5px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        [data-testid="stImage"] img:hover {
            transform: scale(1.05);
            box-shadow: 0 15px 35px rgba(56, 189, 248, 0.4);
        }

        /* Unified Button Styling with Gradient */
        .stButton button, .stDownloadButton button, .stLinkButton a {
            width: 220px !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            padding: 12px 24px !important;
            transition: all 0.3s ease !important;
            border: 2px solid transparent !important;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
        }

        .stButton button:hover, .stDownloadButton button:hover, .stLinkButton a:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4) !important;
        }

        /* Hero Title Styling */
        .hero-title {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            color: #64748b;
            font-weight: 500;
            margin-bottom: 1rem;
        }

        /* Custom Metrics */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem !important;
            font-weight: 700 !important;
            color: #667eea !important;
        }

        /* Skill Cards */
        [data-testid="stVerticalBlock"] > div:has(> div > div[data-testid="stMarkdownContainer"]) {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border-radius: 15px;
            padding: 1.5rem;
            border: 2px solid rgba(102, 126, 234, 0.2);
            transition: all 0.3s ease;
        }

        [data-testid="stVerticalBlock"] > div:has(> div > div[data-testid="stMarkdownContainer"]):hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
            border-color: rgba(102, 126, 234, 0.4);
        }

        /* Expander Styling */
        [data-testid="stExpander"] {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
            border-radius: 15px;
            border: 2px solid rgba(102, 126, 234, 0.15);
            margin-bottom: 1rem;
        }

        /* Container Border Styling */
        [data-testid="stVerticalBlock"] > [data-testid="element-container"] > div[data-testid="stVerticalBlock"] {
            border-radius: 15px !important;
        }

        /* Caption Styling */
        .stCaption {
            color: #64748b !important;
            font-size: 0.95rem !important;
        }

        /* Divider Styling */
        hr {
            margin: 2rem 0 !important;
            border: none !important;
            height: 2px !important;
            background: linear-gradient(90deg, transparent, #667eea, transparent) !important;
        }

        /* Section Headers */
        h3 {
            color: #1e293b !important;
            font-weight: 700 !important;
            margin-bottom: 1.5rem !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Layout
col1, col2 = st.columns([1, 2.5], gap="large")

with col1:
    # Profile Image
    try:
        img = Image.open("assets/sohail_photo.jpeg")
        st.image(img, use_container_width=False)
    except FileNotFoundError:
        st.info("📷 Photo Missing")

    # Action Buttons
    st.link_button("📧 Email Me", "mailto:sohailshaik1712@gmail.com")
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/sohailshaik1107/")
    st.link_button("🐙 GitHub", "https://github.com/sohailshaik1712")

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
    # Hero Section
    st.markdown(
        '<h1 class="hero-title">Hey, I\'m Sohail! 👋</h1>', unsafe_allow_html=True
    )
    st.markdown(
        '<p class="hero-subtitle">Data Platform Engineer | MLOps Enthusiast</p>',
        unsafe_allow_html=True,
    )
    st.caption("📍 Hyderabad, India | System Engineer @ TCS")

    st.write("")

    # Bio
    st.markdown(
        """
        I'm a **System Engineer at TCS**, building robust data platforms for **Diageo's** global operations.

        By day, I architect scalable data pipelines that handle millions of records. By night, I explore the
        fascinating world of **MLOps**, containerization, and CI/CD for machine learning systems.

        My passion lies in bridging the gap between data engineering and machine learning operations,
        creating seamless pipelines that turn data into actionable insights.
        """
    )

    st.write("")

    # Quick Stats
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Experience", "1+ Year", delta="TCS")
    with c2:
        st.metric("Education", "8.42 CGPA", delta="B.Tech")
    with c3:
        st.metric("Projects", "10+", delta="Completed")
    with c4:
        st.metric("Focus", "MLOps", delta="& Data Eng")

st.divider()

# Skills Section
st.markdown("### 🛠️ Technical Expertise")
st.write("")

s1, s2, s3, s4 = st.columns(4)

with s1:
    with st.container(border=True):
        st.markdown("**💻 Programming**")
        st.write("")
        st.caption("🐍 Python")
        st.caption("☕ Java")
        st.caption("🗄️ SQL")
        st.caption("⚡ FastAPI")

with s2:
    with st.container(border=True):
        st.markdown("**🚀 MLOps & DevOps**")
        st.write("")
        st.caption("🐳 Docker")
        st.caption("📊 Kafka")
        st.caption("🔄 CI/CD")
        st.caption("📦 Git")

with s3:
    with st.container(border=True):
        st.markdown("**🗄️ Databases**")
        st.write("")
        st.caption("🐘 PostgreSQL")
        st.caption("💚 MongoDB")
        st.caption("🌟 Neon")
        st.caption("🐬 MySQL")

with s4:
    with st.container(border=True):
        st.markdown("**🤖 ML & AI**")
        st.write("")
        st.caption("🧠 TensorFlow")
        st.caption("🔥 PyTorch")
        st.caption("📚 Scikit-learn")
        st.caption("🎯 Keras")

st.divider()

# Experience Section
st.markdown("### 💼 Professional Experience")
st.write("")

with st.expander("**System Engineer** @ Tata Consultancy Services", expanded=True):
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.caption("**Diageo - Global Data Platform Engineering**")
    with col_b:
        st.caption("📅 June 2024 - Present")

    st.write("")
    st.markdown(
        """
        - 🏗️ **Architected and deployed** scalable data pipelines processing **millions of product records**
          for Diageo's global master data management system
        - 🔧 **Developed enterprise-grade REST APIs** using Java and JavaScript, enabling secure data
          delivery across multiple business units
        - ⚡ **Optimized data workflows** reducing processing time by 40% through efficient pipeline design
        - 🛡️ **Implemented robust security measures** ensuring GDPR and data compliance across all systems
        - 🤝 **Collaborated with cross-functional teams** across 5+ countries to deliver business-critical solutions
        """
    )

st.divider()

# Featured Projects
st.markdown("### 🚀 Featured Projects")
st.write("")

h1, h2 = st.columns(2)

with h1:
    with st.container(border=True):
        st.markdown("#### 🧠 Alzheimer's Disease Detection")
        st.write("")
        st.markdown(
            """
            Advanced deep learning system for early Alzheimer's detection using medical imaging.

            **Highlights:**
            - ✅ **99.23% accuracy** using EfficientNet B0-B6 ensemble
            - 🎯 Multi-class classification across 4 severity stages
            - 🔬 Transfer learning with fine-tuned architectures
            - 📊 Real-time inference pipeline

            **Tech Stack:** TensorFlow, Keras, EfficientNet, Python
            """
        )

with h2:
    with st.container(border=True):
        st.markdown("#### 🎬 Intelligent Movie Recommender")
        st.write("")
        st.markdown(
            """
            Personalized recommendation engine built on collaborative filtering and content-based algorithms.

            **Highlights:**
            - 📈 Trained on **26M+ user ratings** from MovieLens
            - 🎯 Hybrid recommendation approach (collaborative + content)
            - ⚡ Sub-second response time using optimized algorithms
            - 🔍 Smart search with fuzzy matching

            **Tech Stack:** Scikit-learn, Pandas, Streamlit, FastAPI
            """
        )

st.write("")

# Call to Action
st.markdown("---")
cta_col1, cta_col2, cta_col3 = st.columns([1, 2, 1])
with cta_col2:
    st.markdown(
        """
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); border-radius: 15px; border: 2px solid rgba(102, 126, 234, 0.2);">
            <h3 style="color: #667eea; margin-bottom: 1rem;">Let's Build Something Amazing Together! 🚀</h3>
            <p style="color: #64748b; font-size: 1.1rem;">
                Interested in collaborating on data engineering or MLOps projects?<br>
                I'm always open to discussing new opportunities and ideas.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
