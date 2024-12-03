import streamlit as st

st.title("Resultados de la Encuesta")

# variables guardadas
age16_18 = st.session_state["user_age16"]
age13_15 = st.session_state["user_age13"]
st.write(f"tienes de 16 a 18 años", age16_18)
promedioF5 = st.session_state["promedioF5"]
promedioF2 = st.session_state["promedioF2"]
st.write(f"promedio f5 {promedioF5}")


zone = st.session_state['user_home']
home_room = st.session_state['user_home_room']
home_laundry = st.session_state['user_home_laundry']

promedio_mobile = st.session_state['promedio_mobile']
st.write(f" mobile use {promedio_mobile}")

user_gender = st.session_state["user_gender"]
home_cleaning = st.session_state['user_home_cleaning']
home_pets = st.session_state['user_home_pets']

activity_weights_value = st.session_state['user_activity_weights'] 
activity_play_value = st.session_state['user_activity_play']
activity_football_value = st.session_state['user_activity_football']









