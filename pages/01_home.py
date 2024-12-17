import streamlit as st

st.header('Preguntas Sociodemográficas')

user_age = st.radio(
    "¿Cuál es tu edad?:",
    ('10-12', '13-15', '16-18', 'mayor a 18')
)
# Map the selected age category to the desired values
if user_age == '16-18':
    age16_18 = 1
    age13_15  = 0
elif user_age == "13-15":
    age13_15 = 1
    age16_18 = 0
else:
    age16_18 = 0
    age13_15 = 0

# Store in session state
st.session_state["user_age16"] = age16_18
st.session_state["user_age13"] = age13_15

# Inicializar la clave en session_state si no existe
if "user_gender" not in st.session_state:
    st.session_state["user_gender"] = "Femenino"  # Valor por defecto inicial
def change_gender():
    st.session_state["user_gender"] = st.session_state["radio_selection"]

# Widget de selección de género
gender = st.radio(
    "¿Cuál es su género?",
    options=["Femenino", "Masculino", "Otro"],
    key="radio_selection",  # Asigna un valor temporal
    index=["Femenino", "Masculino", "Otro"].index(st.session_state["user_gender"]),
    on_change=change_gender
)

# Mostrar el resultado seleccionado actualmente
st.write(f"Género seleccionado: {st.session_state['user_gender']}")
#st.session_state["user_gender"] = user_gender

# PREGUNTAS RELACIONADAS AL HOGAR
# home area

# Initialize session state keys if they don't exist
if "user_home" not in st.session_state:
    st.session_state["user_home"] = 1  # Default numerical value: 'Urbana' → 1
if "home_selection" not in st.session_state:
    # Remap the numerical value to the corresponding option
    st.session_state["home_selection"] = "Urbana" if st.session_state["user_home"] == 1 else "Rural"

# Function to update session state when selection changes
def update_home():
    st.session_state["user_home"] = 1 if st.session_state["home_selection"] == "Urbana" else 0

# Radio button for zone selection
user_home = st.radio(
    "La zona en que usted vive es:",
    options=["Urbana", "Rural"],
    key="home_selection",
    on_change=update_home
)

# Debugging: Display current values for verification
st.write(f"Zona seleccionada: {st.session_state['home_selection']}")
st.write(f"Valor numérico almacenado: {st.session_state['user_home']}")



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

user_activity_football = st.radio(
    "¿Ha practicado fútbol en los últimos 7 días (última semana)? Si su respuesta es sí, ¿cuántas veces lo ha hecho??:",
    list(opciones_activity.keys())
)


activity_football_value = opciones_activity[user_activity_football]

st.session_state['user_activity_football'] = activity_football_value
