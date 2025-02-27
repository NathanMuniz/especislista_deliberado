#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import EspecialistaDeliberado, CoachDeliberado

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Investimento',
        'objetivo': 'Queor aprender sobre investimentos. E vou estudar 2h por dia sobre. ',
        'hr_inicio': '13:00',
        'hr_fim': '15:00'
    }

    inputs_coach = {
        'atividade_contexto': '**Plano de Estudos Diários (2 horas/dia) para se Tornar um Expert em Investimentos** Este plano utiliza a prática deliberada e intencional, dividindo o aprendizado em sessões de 2 horas, distribuídas ao longo da semana, focando em diferentes módulos de acordo com as fases de aprendizado.  A validação ao final de cada sessão é crucial para reforçar o aprendizado e identificar áreas que precisam de maior atenção. **Fase 1: Fundamentos (6-12 meses) - 2 horas/dia, 5 dias/semana** **(Total de tempo: 10h semanais)** **Semana 1-4: Introdução aos Mercados Financeiros e Análise Fundamentalista Básica** * **Sessão 1 (1 hora):** Leitura de capítulos de "Investimentos" (Gitman & Zutter) ou similar, focando em um conceito específico (ex: tipos de ativos, indicadores financeiros básicos).  **Validação:** Resumo escrito dos conceitos aprendidos e exemplos práticos. * **Sessão 2 (1 hora):** Prática em plataforma online (Investopedia, TradingView): simulação de investimentos com diferentes tipos de ativos.  **Validação:** Relatório de operações simuladas, com justificativas para cada decisão. **Semana 5-8: Análise Técnica Introdutória e Gestão de Risco Básica** * **Sessão 1 (1 hora):** Leitura sobre análise técnica básica (candlesticks, médias móveis) e prática em plataforma online identificando padrões simples.  **Validação:** Identificação e anotação de 5 padrões gráficos em gráficos reais, com explicação do potencial movimento. * **Sessão 2 (1 hora):**  Leitura sobre gestão de risco básica (diversificação, stop-loss) e simulação de carteira diversificada.  **Validação:** Criação de uma carteira simulada diversificada com justificativa das escolhas e definição de stop-loss para cada ativo. **Semana 9-12: Revisão e Aprofundamento dos Fundamentos** * **Sessão 1 (1 hora):** Revisão dos conceitos aprendidos nas semanas anteriores, com foco em exercícios práticos. **Validação:** Teste com perguntas sobre os conceitos-chave e resolução de problemas práticos (ex: cálculo de indicadores financeiros, interpretação de gráficos). * **Sessão 2 (1 hora):** Leitura aprofundada sobre um tópico específico de interesse dentro dos fundamentos. **Validação:**  Apresentação oral ou escrita sobre o tema estudado, demonstrando compreensão e capacidade de aplicação. **(Repetir o ciclo de 12 semanas, aprofundando os temas a cada ciclo.)** **Fase 2: Intermediário (12-24 meses) - 2 horas/dia, 5 dias/semana** **(Total de tempo: 10h semanais)** **Semana 13-16: Análise Fundamentalista Avançada** * **Sessão 1 (1 hora):** Leitura sobre Valuation (DCF) e análise de relatórios financeiros de empresas reais. **Validação:** Cálculo de valuation para uma empresa, justificando as premissas e comparando com o preço de mercado. * **Sessão 2 (1 hora):** Análise de um relatório anual de uma empresa selecionada, focando em análise de concorrência e governança corporativa.  **Validação:**  Resumo escrito dos principais pontos fortes e fracos da empresa analisada. **Semana 17-20: Análise Técnica Aprimorada e Gestão de Risco Sofisticada** * **Sessão 1 (1 hora):** Leitura e prática com indicadores técnicos avançados (RSI, MACD, bandas de Bollinger) e padrões gráficos complexos. **Validação:**  Identificação e análise de 3 padrões gráficos complexos em gráficos reais, com justificativa para entradas e saídas. * **Sessão 2 (1 hora):**  Leitura e simulação de estratégias de hedging. **Validação:**  Proposta de uma estratégia de hedging para uma carteira simulada, considerando diferentes cenários de mercado. **Semana 21-24: Psicologia do Investimento** * **Sessão 1 (1 hora):** Leitura sobre vieses cognitivos e suas implicações nas decisões de investimento. **Validação:**  Identificação e descrição de 3 vieses cognitivos comuns em investimentos, com exemplos práticos. * **Sessão 2 (1 hora):** Prática de exercícios de autoconsciência e gestão emocional durante o processo de tomada de decisões de investimentos simulados. **Validação:**  Registro das emoções e pensamentos durante a simulação de investimento, identificando padrões e áreas de melhoria. **(Repetir o ciclo de 4 semanas com diferentes empresas, relatórios e estratégias, aumentando a complexidade gradualmente)** **Fase 3: Avançado (24+ meses) -  2 horas/dia, 5 dias/semana** **(Total de tempo: 10h semanais)** Esta fase continua a intensificar o aprendizado das fases anteriores, adicionando: * **Alocação de Ativos Estratégica:**  Aplicação prática da Teoria Moderna de Portfólio (MPT), otimização de Markowitz, e construção de carteiras com diferentes perfis de risco. Validação:  Apresentação de uma carteira otimizada, justificando a alocação de ativos e o processo de otimização. * **Networking e Aprendizado Contínuo:**  Participação em eventos do setor, leitura de pesquisas acadêmicas e relatórios de mercado, construção de uma rede de contatos. Validação:  Relatório de atividades de networking e resumo das principais descobertas e insights. * **Desenvolvimento de Estratégias de Investimento Personalizadas:**  Combinação de todas as habilidades para criar estratégias próprias, backtesting e ajustes contínuos. Validação:  Documento com a descrição detalhada da estratégia personalizada, com resultados de backtesting e plano de monitoramento. **Observações:** * Este plano é um guia, e deve ser adaptado às necessidades e ritmo de aprendizado individual. * A prática deliberada em simulações é crucial em todas as fases. * A revisão regular dos conceitos e a busca por novos conhecimentos são essenciais para o sucesso. * A busca por feedback de outros investidores e profissionais da área é altamente recomendada. Lembre-se:  a consistência e a disciplina são fatores cruciais para alcançar a expertise em investimentos.  Este é um processo de longo prazo, que exige dedicação e persistência.',
        'user_goal': 'Hoej irei estudar 3h de investimento',
        'last_progress': """**13:00 - 13:30: Introdução aos Mercados Financeiros (Sessão 1 - Fase 1) - Continuação** **Mensagem 1 (13:00): AÇÃO!**  Retome a leitura do capítulo "Tipos de Ativos" em "Investimentos" (Gitman & Zutter) ou livro equivalente.  Seu objetivo: completar a compreensão dos diferentes tipos de ativos e suas características.  Lembre-se: foco absoluto!  Desligue notificações e elimine distrações. **Mensagem 2 (13:10):  CONCENTRAÇÃO!**  Você está entendendo as nuances entre ações, bonds e fundos? Se surgirem dúvidas, anote-as.  Não deixe que a confusão te impeça de seguir em frente.  Persista! **Mensagem 3 (13:20):  EXECUÇÃO!** Pare a leitura.  Agora, revise o resumo que você escreveu anteriormente.  Adicione informações novas e corrija eventuais erros.  Inclua pelo menos mais dois exemplos práticos para cada tipo de ativo. **Mensagem 4 (13:30): FEEDBACK!** Como você se sente sobre sua compreensão agora?  Quais pontos ainda estão nebulosos?  Descreva suas dificuldades e o que você precisa para avançar.""",
        'topic': 'Investimento',
        # 'objetivo': 'Descrição do que o usuário deseja alcançar',
        'hr_inicio': '13:00',
        'hr_fim': '15'
    }

    
    try:
        # EspecialistaDeliberado().crew().kickoff(inputs=inputs)
        CoachDeliberado().crew().kickoff(inputs=inputs_coach)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()