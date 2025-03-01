import streamlit as st
import pickle
import pandas as pd
import numpy as np
from pages.P01_home import sidebar_style

sidebar_style()

def app():
    st.title("Resultados de la Encuesta")

    #  Ensure session state variable is initialized
    if "calculate_model" not in st.session_state:
        st.session_state.calculate_model = False

    #  Only show the button if calculate_model is False
    if not st.session_state.calculate_model:
        st.write("Por favor, haga clic en 'Finalizar' para ver los resultados.")

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
        'sleep_factor_5': promedioF5, 'home_laundry': home_laundry,
        'sleep_factor_2': promedioF2, 'home_room': home_room,
        'mobile_dependency': promedio_mobile, 'age_group_16-18': age,
        'home_area': zone, 'sleep_factor_3': promedioF3,
        'home_pets': home_pets, 'home_cleaning': home_cleaning,
        'activity_weightlifting': activity_weights_value, 'genre': user_gender,
        'activity_football': activity_football_value
    }

    user_df = pd.DataFrame([user_df])

    def load_model(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    test_models = load_model('best_models.pkl')
    risk_df_xs = load_model('risk_df_xs.pkl')

    score = np.mean([model.predict_proba(user_df)[0, 1] for model in test_models])
    st.write(f"Obtuviste un puntaje de {score}")

    def get_risk_level(score, risk_df):
        for _, row in risk_df.iterrows():
            if row['beg'] <= score <= row['beg'] + row['width']:
                return row['risk_level'], row['real']

    risk_level, risk_value = get_risk_level(score, risk_df_xs)

    risk_mapping = {
        "low risk": "bajo",
        "medium risk": "medio",
        "high risk": "alto",
        "critical risk": "crítico"
    }

    nivel_riesgo = risk_mapping.get(risk_level, "desconocido")

    st.write(f"Tienes un nivel de riesgo **{nivel_riesgo}** con un puntaje de: {risk_value}")

    #  Optional: Reset model calculation if needed
    if st.button("Reiniciar cálculo"):
        st.session_state.calculate_model = False
        st.rerun()