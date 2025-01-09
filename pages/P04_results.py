import streamlit as st
import pickle
import pandas as pd

st.title("Resultados de la Encuesta")
# variables guardadas
age = st.session_state["user_age"]
st.write(f"el usuario tiene {age}")
user_age16 = 1 if age == '16-18' else 0
user_age13 = 1 if age == '13-15' else 0

promedioF5 = st.session_state["promedioF5"]
promedioF2 = st.session_state["promedioF2"]
promedioF3 = st.session_state['promedioF3']

st.write(f"promedio f5 {promedioF5}")


zone = st.session_state['user_home']
st.write(f"vives en una ZONA {zone}")
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

st.write(f"futbol {activity_football_value}")

user_df = {'sleep_factor_5':promedioF5, 'sleep_factor_2':promedioF2, 'sleep_factor_3': promedioF3, 'home_pets': home_pets,
       'home_cleaning':home_cleaning, 'activity_weightlifting':activity_weights_value, 'genre':user_gender, 'activity_playing':activity_play_value,
       'home_laundry':home_laundry, 'home_room':home_room, 'mobile_dependency':promedio_mobile, 'age_group_13-15':user_age13,
       'age_group_16-18':user_age16, 'home_area':zone, 'activity_football':activity_football_value}

print(user_df)
## Modelo 


with open('best_models.pkl', 'rb') as file:
    best_models = pickle.load(file)
    print("best models loaded")

 
## TODO que versiones de pandas,sk,python se usaron

with open('risk_df_xs.pkl', 'rb') as file2:
    probs = pickle.load(file2)
    print("best risk prob loaded")



