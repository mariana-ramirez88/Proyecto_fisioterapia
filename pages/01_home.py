import streamlit as st

st.header('Preguntas Sociodemográficas')

user_age = st.radio(
    "¿Cuál es tu edad?:",
    ('10-12', '13-15', '16-18', 'mayor a 18')
)
if user_age == "16-18":
    age16_18 = 1
    age13_15 = 0
elif user_age == "13-15":
    age16_18 = 0
    age13_15 = 1
else:
    age16_18 = 0
    age13_15 = 0

st.session_state["user_age16"] =  age16_18
st.session_state["user_age13"] =  age13_15


user_gender = st.radio(
    "¿Cuál es su género?",
    ("Femenino","Masculino","Otro")
)
st.session_state["user_gender"] = user_gender

# PREGUNTAS RELACIONADAS AL HOGAR
# home area
user_home = st.radio(
    "La zona en que usted vive es:",
    ('Urbana', 'Rural')
)

if user_home == 'Urbana':
    zone = 1
else: zone = 0

st.session_state['user_home'] = zone


# home room
user_home_room = st.radio(
    "¿Realizas tareas del hogar como tender tu cama o arreglar tu cuarto?:",
    ('Si', 'No')
)

if user_home_room == 'Si':
    home_room = 1
else: home_room = 0

st.session_state['user_home_room'] = home_room

# home laundry
user_home_laundry = st.radio(
    "¿Realizas tareas del hogar como lavar, tender o planchar ropa?:",
    ('Si', 'No')
)

if user_home_laundry == 'Si':
    home_laundry = 1
else: home_laundry = 0
st.session_state['user_home_laundry'] = home_laundry

# home cleaning
user_home_cleaning = st.radio(
    "¿Realizas tareas de limpieza en el hogar como barrer o trapear?:",
    ('Si', 'No')
)

if user_home_cleaning == 'Si':
    home_cleaning = 1
else: home_cleaning = 0
st.session_state['user_home_cleaning'] = home_cleaning


# home pets
user_home_pets = st.radio(
    "¿Realizas tareas relacionadas al paseo cuidado o alimentación de mascotas?:",
    ('Si', 'No')
)

if user_home_pets == 'Si':
    home_pets = 1
else: home_pets = 0
st.session_state['user_home_pets'] = home_pets

st.subheader("Preguntas relacionadas a su actividad fisica en tiempo libre")
opciones_activity = {
    "No":0,
    "1-2 días": 1,
    "3-4 días": 2, 
    "5-6 días": 3, 
    "7 o más días": 4
}

# activity weights
user_activity_weights = st.radio(
    "¿Ha levantado pesas en los últimos 7 días (última semana)? Si su respuesta es sí, ¿cuántas veces lo ha hecho??:",
    list(opciones_activity.keys())
)
# Get the numerical value for the selected option
activity_weights_value = opciones_activity[user_activity_weights]

# Store the result in session state
st.session_state['user_activity_weights'] = activity_weights_value

# activity playing
user_activity_play = st.radio(
    "¿Ha realizado actividades relacionadas al juego en los últimos 7 días (última semana)? Si su respuesta es sí, ¿cuántas veces lo ha hecho??:",
    list(opciones_activity.keys())
)
activity_play_value = opciones_activity[user_activity_play]

st.session_state['user_activity_play'] = activity_play_value

# activity football
user_activity_football = st.radio(
    "¿Ha practicado fútbol en los últimos 7 días (última semana)? Si su respuesta es sí, ¿cuántas veces lo ha hecho??:",
    list(opciones_activity.keys())
)
activity_football_value = opciones_activity[user_activity_football]

st.session_state['user_activity_football'] = activity_football_value
