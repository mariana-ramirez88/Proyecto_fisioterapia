import streamlit as st
import importlib
import os
from assets.sidebar import sidebar_style

# Configuración inicial de la aplicación
st.set_page_config(page_title='Encuesta Usabana', page_icon=":devices:", layout='wide')

# CSS to hide the default sidebar elements
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#Css to change navegation font color 
st.sidebar.markdown(
    "<h3 style='color: white;'>Secciones de la Encuesta</h3>", 
    unsafe_allow_html=True
)

# Cargar la lista de páginas desde la carpeta "pages"
pages_list = ["home"] + [f.replace(".py", "") for f in os.listdir("pages") if f.endswith(".py")]

# Inicializar el estado de la sesión para la página actual
if "page" not in st.session_state:
    st.session_state.page = "home"  # Start with the homepage

# Sidebar selectbox
page_selection = st.sidebar.selectbox(" ", pages_list, index=pages_list.index(st.session_state.page))
if page_selection != st.session_state.page:
    st.session_state.page = page_selection
    st.rerun()

# Cargar la página actual
def load_page(page_name):
    if page_name == "home":
        # Homepage content
        st.title("Encuesta sobre Exposición a Pantallas y Comportamiento Sedentario en Adolescentes")
        st.write("La información suministrada es de carácter privado y no tendrá ninguna calificación, motivo por el que les pedimos responder con la mayor honestidad posible.")
        st.write("Por favor conteste cada pregunta en todas las secciones, al final se le informará que tan porpenso es a sufrir un nivel de dolor determinado.")
    else:
        module = importlib.import_module(f"pages.{page_name}")
        module.app()

current_page = st.session_state.page
load_page(current_page)

# Lógica del botón "Siguiente"
if current_page != "home": #Only show next button when not on the homepage.
    current_index = pages_list.index(current_page)
    if current_index + 1 < len(pages_list):
        if st.button("Siguiente"):
            st.session_state.page = pages_list[current_index + 1]
            st.rerun()  # Recargar la aplicación para mostrar la siguiente página

if "calculate_model" not in st.session_state:
    st.session_state.calculate_model = False

# Estilo de la barra lateral
sidebar_style()