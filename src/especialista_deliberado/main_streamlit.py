import streamlit as st
import warnings
from crew import EspecialistaDeliberado

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(inputs):
    """
    Run the crew with user inputs.
    """
    try:
        EspecialistaDeliberado().crew().kickoff(inputs=inputs)
        st.success("Crew iniciado com sucesso!")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

# Interface Streamlit
st.title("Configuração do CrewAI")

# Inputs do usuário
topic = st.text_input("Tópico", "Investimento")
objetivo = st.text_area("Objetivo", "Quero aprender sobre investimentos. E vou estudar 2h por dia sobre.")
hr_inicio = st.time_input("Horário de início", value=None)
hr_fim = st.time_input("Horário de fim", value=None)

if st.button("Iniciar Crew"):
    if hr_inicio and hr_fim:
        inputs = {
            'topic': topic,
            'objetivo': objetivo,
            'hr_inicio': hr_inicio.strftime('%H:%M'),
            'hr_fim': hr_fim.strftime('%H:%M')
        }
        run(inputs)
    else:
        st.warning("Por favor, selecione horários válidos.")
