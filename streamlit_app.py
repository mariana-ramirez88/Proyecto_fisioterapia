import streamlit as st

# Title of the app
st.title('Encuesta Fisioterapia')

# Ask a question
st.header("Responde las siguientes preguntas:")

# Question
question = "¿Aceptas el tratamiento de datos personales?"
st.write(question)
st.checkbox("Acepto")
# User input (dropdown, radio buttons, or text input)
user_answer = st.radio(
    "¿Cuál es tu edad?:",
    ('10-12', '13-15', '16-18', 'mayor a 18')
)

user_answer2 = st.radio(
    "¿Cuántas horas duermes al dia?:",
    ('5 o menos', '6-8', 'mas de 8')
)

# Button to submit the answer
if st.button("Submit"):
    # Scoring logic
    if user_answer == '10-12':
        score = 4
        st.success(f"Tienes un riesgo bajo de tener dolor crónico: {score}.")
    else:
        score = 1
        st.error(f"Tienes un alto riesgo de dolor crónico: {score}.")
