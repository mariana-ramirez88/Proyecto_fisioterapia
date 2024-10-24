import streamlit as st

def run():
    # Título de la página de resultados
    st.title("Resultados de la Encuesta")

    # Verificar si los resultados están en session_state
    if 'promedioF5' in st.session_state and 'promedioF2' in st.session_state:
        # Recuperar los valores almacenados en session_state
        promedioF5 = st.session_state.get('promedioF5', 0)
        promedioF2 = st.session_state.get('promedioF2', 0)
        accept_data = st.session_state.get('accept_data', False)
        user_age = st.session_state.get('user_age', "No especificada")

        # Mostrar los resultados
        st.header("Respuestas sobre el tratamiento de datos")
        st.write(f"¿Aceptaste el tratamiento de datos?: {'Sí' if accept_data else 'No'}")
        
        st.header("Información demográfica")
        st.write(f"Edad: {user_age}")

        st.header("Resultados de los factores de sueño")
        st.write(f"Promedio de respuestas en Sleep Factor 5: {promedioF5}")
        st.write(f"Promedio de respuestas en Sleep Factor 2: {promedioF2}")
        
        # Puedes agregar más análisis o gráficos si es necesario

    else:
        st.write("Parece que no has completado la encuesta.")

# Llamar a la función
run()
