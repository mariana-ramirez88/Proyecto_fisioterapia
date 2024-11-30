import streamlit as st
import numpy as np
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


# PREGUNTAS RELACIONADAS AL HOGAR
st.subheader('Preguntas Relacionadas al Hogar')
# home area
user_home = st.radio(
    "¿En qué zona vives?:",
    ('Urbana', 'Rural')
)

if user_home == 'Urbana':
    zone = 1
else: zone = 0
# home room
user_home_room = st.radio(
    "¿Realizas tareas del hogar como tender tu cama o arreglar tu cuarto?:",
    ('Si', 'No')
)

if user_home_room == 'Si':
    home_room = 1
else: home_room = 0
# home laundry
user_home_laundry = st.radio(
    "¿Realizas tareas del hogar como lavar, tender o planchar ropa?:",
    ('Si', 'No')
)

if user_home_laundry == 'Si':
    home_laundry = 1
else: home_laundry = 0


# PREGUNTAS RELACIONADAS A mobile use 
st.subheader('Preguntas Relacionadas al uso de dispositivos mobiles ')
st.write('Responde a las siguientes afirmaciones')

def generar_preguntas(preguntas, opciones):
    
    respuestas = []
    for pregunta in preguntas:
        respuesta = st.radio(pregunta, list(opciones.keys()))
        respuestas.append(opciones[respuesta])
    return respuestas

# Diccionario de opciones de respuesta
valores_respuestas_mobile = {
    "nunca": 0,
    "ocasionalmente": 1,
    'frecuentemente': 2,
    'siemrpe':3
}

# Lista de preguntas
preguntas = [
    "Me han llamado la atención o me han hecho alguna advertencia por utilizar mucho el celular",
    "Me he puesto un límite de uso y lo he podido cumplir?",
    "He discutido con algún familiar por el gasto económico que hagp del celular",
    "Dedico más tiempo del que quisieras a usar el celular",
    "Me has pasado (excedido) con el uso del celular"
    ,"Me he acostado más tarde o he dormido menos por estar utilizando el celular",
    "Gasto más dinero con el celular del que me había previsto",
    "Cuando me aburro, utilizo el celular",
    "Utilizo el celular en situaciones que, aunque no son peligrosas, no es correcto hacerlo (comiendo, mientras otras personas me hablan, etc.)",
    "Me han reñido (regañado) por el gasto económico del celular",
    "Cuando llevo un tiempo sin utilizar el celular, siento la necesidad de usarlo (llamar a alguien, enviar un SMS o un WhatsApp, etc.)",
    "Últimamente utilizo mucho más el celular",
    "Si se me estropeara (dañara) el celular durante un periodo largo de tiempo y tardarán en arreglarlo, me encontraría mal",
    "Cada vez necesito utilizar el celular con más frecuencia",
    "Si no tengo el celular me encuentro mal",
    "Cuando tengo el celular a la mano, no puedo dejar de utilizarlo",
    "Nada más levantarme lo primero que hago es ver si me ha llamado alguien al celular, si me han mandado un mensaje, un WhatsApp, etc.",
    "Cuando me siento solo, le hago una llamada a alguien, le envío un mensaje o un WhatsApp, etc. ",
    "Gasto más dinero con el celular ahora que al principio ",
    "Ahora mismo agarraría el celular y enviaría un mensaje, o haría una llamada ",
    "No es suficiente para mí usar el celular como antes, necesito usarlo cada vez más ",
    "No creo que pudiera aguantar una semana sin celular "
]

# Generar preguntas y obtener respuestas
respuestas_mobile = generar_preguntas(preguntas, valores_respuestas_mobile)

# Calcular la media de las respuestas
media_respuestas = np.mean(respuestas_mobile)

st.write(f"El promedio de las respuestas es: {media_respuestas}")




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

