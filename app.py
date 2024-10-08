
import streamlit as st
# Set up the main page
st.sidebar.title("Survey Navigation")
page = st.sidebar.radio("Go to", ["Page 1", "Page 2"])

if page == "Page 1":
    import page_1
elif page == "Page 2":
    import page_2
