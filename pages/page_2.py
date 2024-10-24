import streamlit as st

def run():
    # Título de la página
    st.title('Encuesta Fisioterapia - Página 2')

    # SLEEP FACTOR 5
    st.header("Sleep Factor 5")

    # Valores de respuestas
    valores_respuestasF5 = {
        "sí": 1,
        "no": 0
    }

    # Lista para almacenar las respuestas F5
    respuestasF5 = []

    # Preguntas de SLEEP FACTOR 5
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

    # Calcular el promedio de las respuestas F5
    promedioF5 = sum(respuestasF5) / len(respuestasF5)
    st.write("El promedio de tus respuestas en Sleep Factor 5 es:", promedioF5)

    # Guardar las respuestas de F5 en session_state
    st.session_state.promedioF5 = promedioF5

    # SLEEP FACTOR 2
    st.header("Sleep Factor 2")

    # Lista para almacenar las respuestas F2
    respuestasF2 = []

    # Preguntas de SLEEP FACTOR 2
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

    # Calcular el promedio de las respuestas F2
    promedioF2 = sum(respuestasF2) / len(respuestasF2)
    st.write("El promedio de tus respuestas en Sleep Factor 2 es:", promedioF2)

    # Guardar las respuestas de F2 en session_state
    st.session_state.promedioF2 = promedioF2

    # Botón para continuar a la siguiente página
    if st.button("Next"):
        st.session_state.page = "Page 3"
        st.experimental_rerun()

run()
