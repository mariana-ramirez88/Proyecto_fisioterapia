import streamlit as st
import pickle
import pandas as pd
import numpy as np
from pages.P01_home import sidebar_style
from PIL import Image
import base64
import requests
import uuid
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables del archivo .env



sidebar_style()

def guardar_en_redcap(dataframe):
    API_URL = "https://redcap.unisabana.edu.co/api/"
    API_TOKEN = st.secrets["redCap_token"]  # Obtiene la variable desde streamlit secrets

    if API_TOKEN is None:
        raise ValueError("API_TOKEN no está definido en secrets de streamlit")


    records = dataframe.to_dict(orient='records')
    payload = {
        'token': API_TOKEN,
        'content': 'record',
        'format': 'json',
        'type': 'flat',
        'overwriteBehavior': 'normal',
        'data': str(records).replace("'", '"'),  # JSON válido
        'returnContent': 'count',
        'returnFormat': 'json'
    }

    response = requests.post(API_URL, data=payload)
    return response.json()


def app():
    st.title("Resultados de la Encuesta")

    #  Ensure session state variable is initialized
    if "calculate_model" not in st.session_state:
        st.session_state.calculate_model = False

    #  Only show the button if calculate_model is False
    if not st.session_state.calculate_model:
        st.write("Por favor, haga clic en 'Finalizar' para ver los resultados. Esto puede tomar un tiempo")

        if st.button("Finalizar"):
            st.session_state.calculate_model = True
            st.rerun()  #  Force a rerun to update state
        return  # Important: Stop execution here until button is clicked

    # ✅ Code below only runs AFTER the button is clicked
    age = st.session_state["user_age"]
    promedioF5 = st.session_state["promedioF5"]
    promedioF2 = st.session_state["promedioF2"]
    promedioF3 = st.session_state["promedioF3"]
    zone = st.session_state["user_home"]
    home_room = st.session_state["user_home_room"]
    home_laundry = st.session_state["user_home_laundry"]
    promedio_mobile = st.session_state["promedio_mobile"]
    user_gender = st.session_state["user_gender"]
    home_cleaning = st.session_state["user_home_cleaning"]
    home_pets = st.session_state["user_home_pets"]
    activity_weights_value = st.session_state["user_activity_weights"]
    activity_play_value = st.session_state["user_activity_play"]
    activity_football_value = st.session_state["user_activity_football"]

    user_df = {
        "record_id" : str(uuid.uuid4()),
        'sleep_factor_5': promedioF5, 'home_laundry': home_laundry,
        'sleep_factor_2': promedioF2, 'home_room': home_room,
        'mobile_dependency': promedio_mobile, 'age_group_16-18': age,
        'home_area': zone, 'sleep_factor_3': promedioF3,
        'home_pets': home_pets, 'home_cleaning': home_cleaning,
        'activity_weightlifting': activity_weights_value, 'genre': user_gender,
        'activity_football': activity_football_value
    }

    user_df = pd.DataFrame([user_df])

     # ✅ Guardar en REDCap
    user_df.columns = user_df.columns.str.replace('-', '_')
    redcap_result = guardar_en_redcap(user_df)
    # evita problemas con nombres en re cap
    # ✅ Renombrar solo la columna necesaria para el modelo
    user_df_for_prediction = user_df.rename(columns={'age_group_16_18': 'age_group_16-18'})
    user_df_for_prediction = user_df_for_prediction.drop(columns=['record_id'])

    def load_model(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    test_models = load_model('best_models.pkl')
    risk_df_xs = load_model('risk_df_xs.pkl')

    score = np.mean([model.predict_proba(user_df_for_prediction)[0, 1] for model in test_models])
    #st.write(f"Obtuviste un puntaje de {score}")

    def get_risk_level(score, risk_df):
        for _, row in risk_df.iterrows():
            if row['beg'] <= score <= row['beg'] + row['width']:
                return row['risk_level'], row['real']

    risk_level, risk_value = get_risk_level(score, risk_df_xs)
    # 4. Añadir resultados al mismo record
    user_df["risk_value"] = risk_value
    user_df["risk_level"] = risk_level

    # 5. Guardar nuevamente en REDCap
    guardar_en_redcap(user_df)

    risk_mapping = {
    "low risk": "Tienes un nivel de riesgo BAJO",
    "medium risk": "Tienes un nivel de riesgo MEDIO",
    "high risk": "Tienes un nivel de riesgo ALTO",
    "critical risk": "Tienes un nivel de riesgo CRÍTICO"
    }

    color_mapping = {
        "bajo": "green",
        "medio": "yellow",
        "alto": "orange",
        "crítico": "red"
    }

    # Determinar el texto completo del nivel de riesgo
    texto_riesgo = risk_mapping.get(risk_level, "Nivel de riesgo DESCONOCIDO")
    nivel_riesgo = texto_riesgo.split()[-1].lower()

    # Determinar el color correspondiente
    color = color_mapping.get(nivel_riesgo, "grey")

    # Mostrar la probabilidad
    st.write(f"Tienes una probabilidad de **{risk_value * 100:.0f}%** de padecer dolor musculoesquelético")

    # Mostrar el texto completo del riesgo con la barra de color
    st.markdown(
        f"<div style='padding: 10px; border-radius: 5px; background-color: {color}; color: black; text-align: center; font-weight: bold;'>"
        f"{texto_riesgo}"
        f"</div>",
        unsafe_allow_html=True
    )

    with open("recomendaciones.jpeg", "rb") as imagen:
        img_base64 = base64.b64encode(imagen.read()).decode()

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/jpeg;base64,{img_base64}" style="max-width:100%; height:auto;"/>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Regresar ⬅️",key="button4"):
        st.session_state.page = "P03_mobile"  # Avanzar a la siguiente página
        st.rerun()
