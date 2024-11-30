import streamlit as st


# PREGUNTAS RELACIONADAS AL HOGAR
st.header('Preguntas Relacionadas al Hogar')
# home area
user_home = st.radio(
    "¿En qué zona vives?:",
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
