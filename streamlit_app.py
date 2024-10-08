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

st.subheader('Preguntas Relacionadas al Sueño')

# Question 3: Sleep Factor 5
valores_respuestasF5 = {
    "sí": 1,
    "no": 0
}

# Lista para almacenar las respuestas
respuestasF5 = []

# Preguntas de sueño
# SLEEP FACTOR 5
user_sleepF5_1 = st.radio(
    "¿Despiertas más cansado de lo que estabas antes de acostarte?",
    list(valores_respuestasF5.keys())
)
respuestasF5.append(valores_respuestasF5[user_sleepF5_1])

user_sleepF5_2 = st.radio(
    "¿Te sientes cansado la mayor parte del día?",
    list(valores_respuestasF5.keys())
)
respuestasF5.append(valores_respuestasF5[user_sleepF5_2])

user_sleepF5_3 = st.radio(
    "¿Fue difícil levantarte en la mañana?",
    list(valores_respuestasF5.keys())
)
respuestasF5.append(valores_respuestasF5[user_sleepF5_3])

user_sleepF5_4 = st.radio(
    "¿Sientes necesidad de acostarte y levantarte más tarde que los demás?",
    list(valores_respuestasF5.keys())
)
respuestasF5.append(valores_respuestasF5[user_sleepF5_4])

# Calcular el promedio de las respuestas 
if respuestasF5:  
    promedioF5 = sum(respuestasF5) / len(respuestasF5)
    st.write("El promedio de tus respuestas es:", promedioF5)

# SLEEP FACTOR 2
# Lista para almacenar las respuestas
respuestasF2 = []
# opciones de respuesta iguales a F5

user_sleepF2_1 = st.radio(
    "¿Tuviste pesadillas?",
    list(valores_respuestasF5.keys())
)
respuestasF2.append(valores_respuestasF5[user_sleepF2_1])

user_sleepF2_2 = st.radio(
    "¿Despertaste con miedo?",
    list(valores_respuestasF5.keys())
)
respuestasF2.append(valores_respuestasF5[user_sleepF2_2])

user_sleepF2_3 = st.radio(
    "¿Despertaste sudando por algo que soñaste?",
    list(valores_respuestasF5.keys())
)
respuestasF2.append(valores_respuestasF5[user_sleepF2_3])

user_sleepF2_4 = st.radio(
    "¿Soñaste con algo que te dio miedo?",
    list(valores_respuestasF5.keys())
)
respuestasF2.append(valores_respuestasF5[user_sleepF2_4])


# Calcular el promedio de las respuestas 
if respuestasF2:  
    promedioF2 = sum(respuestasF2) / len(respuestasF2)
    st.write("El promedio de tus respuestas es:", promedioF2)





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

