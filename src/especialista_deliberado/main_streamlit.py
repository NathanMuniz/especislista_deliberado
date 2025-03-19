import streamlit as st
import warnings
from crew import Testcrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(inputs):
    """Run the crew with user inputs."""
    try:
        result = Testcrew().crew().kickoff(inputs=inputs)
        st.success("Crew iniciado com sucesso!")
        return result
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")

# Sidebar navigation
st.sidebar.title("Navegação")
st.sidebar.page_link("main_streamlit.py", label="Início")
st.sidebar.page_link("pages/about.py", label="Sobre o Projeto")

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
        markdown_output = run(inputs)
        st.markdown(markdown_output)
    else:
        st.warning("Por favor, selecione horários válidos.")
