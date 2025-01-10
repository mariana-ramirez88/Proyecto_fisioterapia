import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.title("Resultados de la Encuesta")
# variables guardadas
age = st.session_state["user_age"]

promedioF5 = st.session_state["promedioF5"]
promedioF2 = st.session_state["promedioF2"]
promedioF3 = st.session_state['promedioF3']


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

user_df = {'sleep_factor_5':promedioF5, 'home_laundry':home_laundry, 'sleep_factor_2':promedioF2, 'home_room':home_room,
           'mobile_dependency':promedio_mobile,  'age_group_16-18':age,  'home_area':zone,'sleep_factor_3': promedioF3, 'home_pets': home_pets,
       'home_cleaning':home_cleaning, 'activity_weightlifting':activity_weights_value, 'genre':user_gender, 'activity_football':activity_football_value}

     ### 'activity_playing':activity_play_value, 'age_group_13-15':user_age13}"""

print(user_df)
## Modelo 
user_df = pd.DataFrame([user_df])
# Definimos una función para cargarlo
def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
    
# cargamos los modelos y el risk_df
test_models = load_model('best_models.pkl')
risk_df_xs = load_model('risk_df_xs.pkl')


score = np.mean([model.predict_proba(user_df)[0,1] for model in test_models])
st.write(score)

def get_risk_level(score, risk_df):
    for index, row in risk_df.iterrows():
        if score>=row['beg'] and score<=row['beg']+row['width']:
            return row['risk_level'], row['real']
    

risk_level, risk_value = get_risk_level(score, risk_df_xs)
st.write(f"tienes un nivel de riesgo {risk_level} con un puntaje de: {risk_value}")