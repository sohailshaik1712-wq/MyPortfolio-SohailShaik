import requests
import streamlit as st
from services.api import login

st.title("Admin Login")


# If already logged in
if "token" in st.session_state and st.session_state.token:
    st.success("Already logged in")
    st.info("Go to Admin Panel from sidebar.")
    st.stop()


# Inputs
user = st.text_input("Username")
pwd = st.text_input("Password", type="password")


# Login Button
if st.button("Login"):
    if not user or not pwd:
        st.warning("Enter username and password")
        st.stop()

    try:
        res = login(user, pwd)

        if res.status_code == 200:
            st.session_state.token = res.json()["access_token"]

            st.success("Login successful")

            # Refresh app
            st.rerun()

        elif res.status_code == 401:
            st.error("Invalid username or password")

        else:
            st.error(f"Login failed ({res.status_code})")

    except requests.exceptions.ConnectionError:
        st.error("Backend server not running")

    except Exception as e:
        st.error(f"Unexpected error: {e}")
