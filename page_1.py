import streamlit as st

def run():
    st.title("Page 1")
    st.write("Welcome to the first section of the survey!")
    # Add your survey questions here
    name = st.text_input("What is your name?")
    age = st.number_input("What is your age?", min_value=0)

    if st.button("Next"):
        st.session_state.name = name
        st.session_state.age = age
        st.session_state.page = "Page 2"
        st.experimental_rerun()

run()
