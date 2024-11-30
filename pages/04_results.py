import streamlit as st

st.title("Resultados de la Encuesta")

# variables guardadas
user_age = st.session_state['user_age'] 
st.write(f"tienes {user_age} años")
promedioF5 = st.session_state["promedioF5"]
promedioF2 = st.session_state["promedioF2"]
st.write(f"promedio f5 {promedioF5}")


zone = st.session_state['user_home']
home_room = st.session_state['user_home_room']
home_laundry = st.session_state['user_home_laundry']

promedio_mobile = st.session_state['promedio_mobile']
st.write(f" mobile use {promedio_mobile}")






