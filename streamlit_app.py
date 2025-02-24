import streamlit as st
from assets.sidebar import sidebar_style
# Encabezado app
st.set_page_config(page_title='Encuesta Usabana', page_icon=":devices:",layout='wide')

#titulo
st.title("Encuesta sobre Exposición a Pantallas y Comportamiento Sedentario en Adolescentes ")
st.write("La información suministrada es de carácter privado y no tendrá ninguna calificación, motivo por el que les pedimos responder con la mayor honestidad posible.")

st.write("Por favor conteste cada pregunta en todas las secciones, al final se le informará que tan porpenso es a sufrir un nivel de dolor determinado")

sidebar_style()