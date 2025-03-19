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

    
    try:
        EspecialistaDeliberado().crew().kickoff(inputs=inputs)
        # CoachDeliberado().crew().kickoff(inputs=inputs_coach)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()