import streamlit as st

def run():
    # Título de la encuesta
    st.title('Encuesta Fisioterapia')

    # Instrucciones para el usuario
    st.header("Responde las siguientes preguntas:")

    # Pregunta 1: Aceptación del tratamiento de datos
    question = "¿Aceptas el tratamiento de datos personales?"
    st.write(question)
    accept_data = st.checkbox("Acepto")  # Almacena la entrada del checkbox

    # Pregunta 2: Grupo de edad
    user_age = st.radio(
        "¿Cuál es tu edad?:",
        ('10-12', '13-15', '16-18', 'mayor a 18')
    )

    # Guardar respuestas al hacer clic en "Next"
    if st.button("Siguiente"):
        # Almacena las respuestas en session_state
        st.session_state.accept_data = accept_data
        st.session_state.user_age = user_age
        st.session_state.page = "Page 2"  # Cambiar a la siguiente página
        st.experimental_rerun()  # Recargar la aplicación

# Llamada a la función
run()
