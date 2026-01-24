# 1. Updated CSS for centered alignment
import streamlit as st
from PIL import Image

# 1. Advanced CSS for Zero-Gap Centering
st.markdown(
    """
    <style>
        /* 1. Eliminate the gap between elements in the sidebar column */
        [data-testid="column"]:nth-of-type(1) [data-testid="stVerticalBlock"] {
            gap: 0rem !important;
            align-items: center;
        }

        /* 2. Fixed Circular Image with tight bottom margin */
        [data-testid="stImage"] img {
            border-radius: 50%;
            border: 4px solid #38bdf8;
            object-fit: cover;
            aspect-ratio: 1 / 1;
            width: 220px;
            height: 220px;
            margin-bottom: 15px; /* Manually control the space here */
        }

        /* 3. Button Styling: Force uniform width and remove default top margins */
        .stButton, .stDownloadButton, .stLinkButton {
            margin-top: -5px !important; /* Pulls buttons closer together */
            width: 100%;
            display: flex;
            justify-content: center;
        }

        .stButton button, .stDownloadButton button, .stLinkButton a {
            width: 220px !important; /* Matches image width for perfect vertical lines */
            border-radius: 8px !important;
            padding: 0.5rem !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 2. Re-rendering the layout
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Centered Circular Photo
    try:
        img = Image.open("assets/sohail_photo.jpeg")
        st.image(img)
    except Exception:
        st.info("📷 Photo Missing")

    # Action Buttons (Now tightly packed)
    st.link_button("📧 Email Me", "mailto:sohailshaik1712@gmail.com")
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/sohailshaik1107/")

    try:
        with open("assets/Sohail-Shaik-Resume.pdf", "rb") as f:
            resume_bytes = f.read()
        st.download_button(
            label="📄 Download Resume",
            data=resume_bytes,
            file_name="Sohail-Shaik-Resume.pdf",
            mime="application/pdf",
        )
    except FileNotFoundError:
        st.caption("Resume not found.")

with col2:
    st.title("Hey, I'm Sohail! 👋")
    st.write("### Data Platform Engineer | MLOps Hobbyist")
    st.info("📍 Hyderabad, India")

    st.write(
        """
        I’m a **System Engineer at TCS** who loves the "Ops" in MLOps.
        Professionally, I build heavy-duty data platforms and master data pipelines.
        As a hobby, I obsess over model monitoring and CI/CD for ML.

        Basically, I build the tracks *and* the trains for data-driven intelligence! 🚄💨
        """
    )

    # Key Metrics as small badges
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.caption("EXPERIENCE")
            st.markdown("**TCS / Diageo**")
    with c2:
        with st.container(border=True):
            st.caption("EDUCATION")
            st.markdown("**8.42 CGPA**")
    with c3:
        with st.container(border=True):
            st.caption("HOBBY")
            st.markdown("**MLOps Wizardry**")
st.divider()

# 3. The "Dual Life" Skill Grid
st.markdown("### 🛠️ My Toolkit")
s1, s2, s3 = st.columns(3)

with s1:
    with st.container(border=True):
        st.markdown("**Platform Gear**")
        st.caption("Stibo STEP, SAP, Azure AI")
        st.markdown("**The Staples**")
        st.caption("Python, Java, SQL, Git")

with s2:
    with st.container(border=True):
        st.markdown("**MLOps Fun**")
        st.caption("Docker, Kafka, Model CI/CD")
        st.markdown("**Deep Learning**")
        st.caption("EfficientNet, CNN, TensorFlow")

with s3:
    with st.container(border=True):
        st.markdown("**Databases**")
        st.caption("Postgres, MySQL, SQLite")  # [cite: 11]
        st.markdown("**Frameworks**")
        st.caption("FastAPI, Next.js, Streamlit")  # [cite: 12]

st.divider()

# 4. Professional Experience (The Serious Stuff)
st.markdown("### 💼 The Professional Side")
with st.expander("System Engineer @ Tata Consultancy Services", expanded=True):
    st.write("06/2024 - Present | Client: Diageo")
    st.write(
        "* **Data Pipelines**: Engineered scalable pipelines for global product master data."
    )
    st.write(
        "* **Backend Mastery**: Built Java/JS REST APIs for secure enterprise data delivery."
    )
    st.write(
        "* **Automation**: Applied algorithmic rules to automate data quality and governance."
    )

st.divider()

# 5. Project Highlights (The Fun Stuff)
st.markdown("### 🚀 Passion Projects")
h1, h2 = st.columns(2)

with h1:
    with st.container(border=True):
        st.markdown("**🧠 Alzheimer's Stage Detection**")
        st.write(
            "Achieved 99.23% accuracy using EfficientNet B0-B6. More importantly, I built a Streamlit app to visualize the results!"
        )

with h2:
    with st.container(border=True):
        st.markdown("**🎬 Movie Recommender**")
        st.write(
            "Personalized engine handling 26M+ ratings. Content-based filtering at its finest, wrapped in a user-friendly UI."
        )
