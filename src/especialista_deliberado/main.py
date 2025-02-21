#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import EspecialistaDeliberado

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Musíca',
        'objetivo': 'Quero aprender música do zero. Irei estudar 3h por dia. '
    }
    
    try:
        EspecialistaDeliberado().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()