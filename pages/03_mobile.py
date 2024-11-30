import streamlit as st 
import numpy as np
# PREGUNTAS RELACIONADAS A mobile use 
st.subheader('Preguntas Relacionadas al uso de dispositivos mobiles ')
st.write('Responde a las siguientes afirmaciones')

def generar_preguntas(preguntas, opciones):
    
    respuestas = []
    for pregunta in preguntas:
        respuesta = st.radio(pregunta, list(opciones.keys()))
        respuestas.append(opciones[respuesta])
    return respuestas

# Diccionario de opciones de respuesta
valores_respuestas_mobile = {
    "nunca": 0,
    "ocasionalmente": 1,
    'frecuentemente': 2,
    'siemrpe':3
}

# Lista de preguntas
preguntas = [
    "Me han llamado la atención o me han hecho alguna advertencia por utilizar mucho el celular",
    "Me he puesto un límite de uso y lo he podido cumplir?",
    "He discutido con algún familiar por el gasto económico que hagp del celular",
    "Dedico más tiempo del que quisieras a usar el celular",
    "Me has pasado (excedido) con el uso del celular"
    ,"Me he acostado más tarde o he dormido menos por estar utilizando el celular",
    "Gasto más dinero con el celular del que me había previsto",
    "Cuando me aburro, utilizo el celular",
    "Utilizo el celular en situaciones que, aunque no son peligrosas, no es correcto hacerlo (comiendo, mientras otras personas me hablan, etc.)",
    "Me han reñido (regañado) por el gasto económico del celular",
    "Cuando llevo un tiempo sin utilizar el celular, siento la necesidad de usarlo (llamar a alguien, enviar un SMS o un WhatsApp, etc.)",
    "Últimamente utilizo mucho más el celular",
    "Si se me estropeara (dañara) el celular durante un periodo largo de tiempo y tardarán en arreglarlo, me encontraría mal",
    "Cada vez necesito utilizar el celular con más frecuencia",
    "Si no tengo el celular me encuentro mal",
    "Cuando tengo el celular a la mano, no puedo dejar de utilizarlo",
    "Nada más levantarme lo primero que hago es ver si me ha llamado alguien al celular, si me han mandado un mensaje, un WhatsApp, etc.",
    "Cuando me siento solo, le hago una llamada a alguien, le envío un mensaje o un WhatsApp, etc. ",
    "Gasto más dinero con el celular ahora que al principio ",
    "Ahora mismo agarraría el celular y enviaría un mensaje, o haría una llamada ",
    "No es suficiente para mí usar el celular como antes, necesito usarlo cada vez más ",
    "No creo que pudiera aguantar una semana sin celular "
]

# Generar preguntas y obtener respuestas
respuestas_mobile = generar_preguntas(preguntas, valores_respuestas_mobile)

# Calcular la media de las respuestas
promedio_mobile = np.mean(respuestas_mobile)

st.session_state['promedio_mobile'] = promedio_mobile
