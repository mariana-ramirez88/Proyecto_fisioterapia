import streamlit as st
import numpy as np

st.subheader('Preguntas Relacionadas al Sueño')
st.write("Responda Con qué frecuencia en días, en la última semana, le sucedieron los siguientes eventos:")

# Question 3: Sleep Factor 5
valores_respuestasF5 = {
    "0 días": 0,
    "1-2 días": 1,
    '3-4 días': 2,
    '5-6 días':3
}

# Lista para almacenar las respuestas
respuestasF5 = []

# Preguntas de sueño
# SLEEP FACTOR 5
user_sleepF5_1 = st.radio(
    "Despertó más cansado que cuando se acostó",
    list(valores_respuestasF5.keys())
)
respuestasF5.append(valores_respuestasF5[user_sleepF5_1])

user_sleepF5_2 = st.radio(
    "Sintió cansancio la mayor parte del día",
    list(valores_respuestasF5.keys())
)
respuestasF5.append(valores_respuestasF5[user_sleepF5_2])

user_sleepF5_3 = st.radio(
    "Fue difícil levantarse en la mañana",
    list(valores_respuestasF5.keys())
)
respuestasF5.append(valores_respuestasF5[user_sleepF5_3])

user_sleepF5_4 = st.radio(
    "Sintió necesidad de acostarse y levantarse más tarde que los demás",
    list(valores_respuestasF5.keys())
)
respuestasF5.append(valores_respuestasF5[user_sleepF5_4])

# Calcular el promedio de las respuestas 
if respuestasF5:  
    promedioF5 = sum(respuestasF5) / len(respuestasF5)
else: 
    promedioF5 = 0
st.session_state['promedioF5'] = promedioF5


# SLEEP FACTOR 2
# Lista para almacenar las respuestas
respuestasF2 = []
# opciones de respuesta iguales a F5

user_sleepF2_1 = st.radio(
    "Tuvo pesadillas",
    list(valores_respuestasF5.keys())
)
respuestasF2.append(valores_respuestasF5[user_sleepF2_1])

user_sleepF2_2 = st.radio(
    "Despertó con miedo",
    list(valores_respuestasF5.keys())
)
respuestasF2.append(valores_respuestasF5[user_sleepF2_2])

user_sleepF2_3 = st.radio(
    "Despertó sudando por algo que soñó",
    list(valores_respuestasF5.keys())
)
respuestasF2.append(valores_respuestasF5[user_sleepF2_3])

user_sleepF2_4 = st.radio(
    "Soñó algo que le dio miedo",
    list(valores_respuestasF5.keys())
)
respuestasF2.append(valores_respuestasF5[user_sleepF2_4])


# Calcular el promedio de las respuestas 
if respuestasF2:  
    promedioF2 = sum(respuestasF2) / len(respuestasF2)
else: 
        promedioF2 = 0

st.session_state['promedioF2'] = promedioF2

def generar_preguntas(preguntas, opciones):
    
    respuestas = []
    for pregunta in preguntas:
        respuesta = st.radio(pregunta, list(opciones.keys()))
        respuestas.append(opciones[respuesta])
    try:
        return np.mean(respuestas)
    except: 
        return 0

preguntas_F3 = [
     "Despertó porque se atragantó",
     "Le dijeron que despertó llorando pero usted no se acuerda",
     "Despertó y sintió que no podía moverse",
     "Le dijeron que despertó asustado/a y gritando pero usted no se acuerda",
     "Roncó (se lo dijeron o lo sabe)"
]
valores_F3 = {
    "0 días":0,
    "1-2 días": 1,
    "3-4 días": 2, 
    "5-6 días": 3, 
}

promedioF3 = generar_preguntas(preguntas_F3, valores_F3)
st.session_state['promedioF3'] = promedioF3




   

