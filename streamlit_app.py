import streamlit as st

# Title of the app
st.title('Encuesta Fisioterapia')

# Ask a question
st.header("Responde las siguientes preguntas:")

# Question 1: Accepting data treatment
question = "¿Aceptas el tratamiento de datos personales?"
st.write(question)
accept_data = st.checkbox("Acepto")  # Store checkbox input

# Question 2: Age group
user_age = st.radio(
    "¿Cuál es tu edad?:",
    ('10-12', '13-15', '16-18', 'mayor a 18')
)

# Question 3: Sleep hours
user_sleep = st.radio(
    "¿Cuántas horas duermes al día?:",
    ('5 o menos', '6-8', 'más de 8')
)

# Button to submit the answers
if st.button("Submit"):
    if not accept_data:
        st.warning("Por favor acepta el tratamiento de datos personales.")
    else:
        # Scoring logic based on age
        if user_age == '10-12':
            score = 4
            st.success(f"Tienes un riesgo bajo de tener dolor crónico: {score}.")
        else:
            score = 1
            st.error(f"Tienes un alto riesgo de dolor crónico: {score}.")
        
        # Displaying user's sleep data
        st.write(f"Has indicado que duermes {user_sleep} horas al día.")
