import streamlit as st

def run():
    st.title("Page 3")
    st.write("This is the final section of the survey!")
    st.write("Summary of your responses:")
    st.write(f"Name: {st.session_state.get('name', '')}")
    st.write(f"Age: {st.session_state.get('age', '')}")
    st.write(f"Feedback: {st.session_state.get('feedback', '')}")

    if st.button("Submit"):
        # Add your submission logic here
        st.success("Thank you for completing the survey!")

run()
