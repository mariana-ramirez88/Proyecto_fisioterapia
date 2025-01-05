import streamlit as st
import numpy as np

st.subheader('Preguntas Relacionadas al Sueño')
st.write("Responda Con qué frecuencia en días, en la última semana, le sucedieron los siguientes eventos:")

def initialize_radio_var(question, session_key, radio_key, answers, ans_list = "answers list", default_value_map=None, average_key = "average"):
    
    if ans_list not in st.session_state:
        st.session_state[ans_list] = {}

        # Function to calculate the average dynamically based on current responses
    def calculate_average(response_list_key):
        # Extract only numeric values (assuming the values in the dictionary are numeric)
        numeric_values = [value for value in st.session_state[response_list_key].values() if isinstance(value, (int, float))]
        if numeric_values:
            try:
                return sum(numeric_values) / len(numeric_values)
            except:
                return 0
        return 0

    if default_value_map:
        # When there is a numerical mapping for answers
        if session_key not in st.session_state:
            st.session_state[session_key] = default_value_map[answers[0]]

        if radio_key not in st.session_state:
            # Reverse mapping to selected stored answer
            reverse_map = {v: k for k, v in default_value_map.items()}
            selected_option = reverse_map.get(st.session_state[session_key], answers[0])
            st.session_state[radio_key] = selected_option

        def update_variable():
            st.session_state[session_key] = default_value_map[st.session_state[radio_key]]
            # Update the response list dictionary with the session_key and the selected answer
            st.session_state[ans_list][session_key] = st.session_state[session_key]

             # Calculate and display the average after the answer change
            average = calculate_average(ans_list)
            st.session_state[average_key] = average
            st.write(f"Average: {average_key}: {average}")
            
        st.radio(
            question, options=answers, key=radio_key, on_change=update_variable
        )
    else:
        # When no mapping is provided
        if session_key not in st.session_state:
            st.session_state[session_key] = answers[0]

        if radio_key not in st.session_state:
            # Synchronize radio_key with session_key
            st.session_state[radio_key] = st.session_state[session_key]

        def update_variable():
            st.session_state[session_key] = st.session_state[radio_key]
            # Update the response list dictionary with the session_key and the selected answer
            st.session_state[ans_list][session_key] = st.session_state[session_key]
            # Calculate and store the average under a unique key
            average = calculate_average(ans_list)
            st.session_state[average_key] = average  # Store average in session state with the unique key
            st.write(f"Average ({average_key}): {average}")
        st.radio(question, options=answers, key=radio_key, on_change=update_variable)


questionsF5 = ["Despertó más cansado que cuando se acostó","Sintió cansancio la mayor parte del día", "Fue difícil levantarse en la mañana",
"Sintió necesidad de acostarse y levantarse más tarde que los demás"]
session_keys = ['userF5.1', 'userF5.2', 'userF5.3', 'userF5.4']
radio_keys = ['sleepF5.1','sleepF5.2', 'sleepF5.3','sleepF5.4']

# Question 3: Sleep Factor 5
valores_respuestasF5 = {
    "0 días": 0,
    "1-2 días": 1,
    '3-4 días': 2,
    '5-6 días':3
}

# Lista para almacenar las respuestas
respuestasF5 = []

def make_questions(questions, session_keys, radio_keys, mapping, answers_list: str, average_name: str):
    for i in range(len(questions)):
        initialize_radio_var(
            question=questions[i],
            session_key=session_keys[i],
            radio_key=radio_keys[i],
            answers= list(mapping.keys()),
            ans_list=answers_list,
            default_value_map=mapping,
            average_key=average_name)
    
make_questions(questionsF5,session_keys,radio_keys,valores_respuestasF5,"respuestasF5","promedioF5")

# SLEEP FACTOR 2
# Lista para almacenar las respuestas
questionsF2 = ["Tuvo pesadillas", "Despertó con miedo","Despertó sudando por algo que soñó", "Soñó algo que le dio miedo"]
session_keysF2 = ['userF2.1', 'userF2.2', 'userF2.3', 'userF2.4']
radio_keysF2 = ['sleepF2.1','sleepF2.2', 'sleepF2.3','sleepF2.4']
# opciones de respuesta iguales a F5
respuestasF2 = []
make_questions(questionsF2,session_keysF2,radio_keysF2,valores_respuestasF5,"respuestasF2","promedioF2")

preguntas_F3 = [
     "Despertó porque se atragantó",
     "Le dijeron que despertó llorando pero usted no se acuerda",
     "Despertó y sintió que no podía moverse",
     "Le dijeron que despertó asustado/a y gritando pero usted no se acuerda",
     "Roncó (se lo dijeron o lo sabe)"
]
valores_F3 = {
    "0 días":0,
    "1-2 días": 1,
    "3-4 días": 2, 
    "5-6 días": 3, 
}

session_keysF3 = ['userF3.1', 'userF3.2', 'userF3.3', 'userF3.4', 'userF3.5']
radio_keysF3 = ['sleepF3.1','sleepF3.2', 'sleepF3.3','sleepF3.4','sleepF3.5']
respuestasF3 = []
make_questions(preguntas_F3,session_keysF3,radio_keysF3,valores_F3,"respuestasF3","promedioF3")



   
