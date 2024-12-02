import streamlit as st
import numpy as np

# Question 2: Age group
user_age = st.radio(
    "¿Cuál es tu edad?:",
    ('10-12', '13-15', '16-18', 'mayor a 18')
)
st.session_state['user_age'] = user_age

st.subheader('Preguntas Relacionadas al Sueño')

# Question 3: Sleep Factor 5
valores_respuestasF5 = {
    "nunca": 0,
    "ocasionalmente": 1,
    'frecuentemente': 2,
    'siempre':3
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
    st.session_state['promedioF5'] = promedioF5


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
    st.session_state['promedioF2'] = promedioF2


   

