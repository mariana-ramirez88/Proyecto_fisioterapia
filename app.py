
import streamlit as st
# Set up the main page
st.sidebar.title("Encuesta Fisioterapia")
page = st.sidebar.radio("Ir a", ["Sección 1", "Sección 2","Sección 3"])

if page == "Sección 1":
    import page_1
if page == "Sección 2":
    import page_2
elif page == "Sección 3":
    import page_3
