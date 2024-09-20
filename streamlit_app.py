import streamlit as st

# Title of the app
st.title('Encuesta Fisioterapia')

# Ask a question
st.header("Responde las siguientes preguntas:")

# Question
question = "¿Cuántas horas duermes al día?"
st.write(question)
st.selectbox('Select', ["menos de 5","entre 6 y 8","más de 8"])

# User input (dropdown, radio buttons, or text input)
user_answer = st.radio(
    "¿Cuál es tu edad?:",
    ('10-12', '13-15', '16-18', 'mayor a 18')
)

# Button to submit the answer
if st.button("Submit"):
    # Scoring logic
    if user_answer == '10-12':
        score = 100/4
        st.success(f"Correct! Your score is {score}.")
    else:
        score = 0
        st.error(f"Incorrect! Your score is {score}.")
