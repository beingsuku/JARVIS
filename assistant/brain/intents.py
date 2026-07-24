"""
Intent definitions: maps trigger keywords to a skill module.
This is deliberately simple (keyword matching) for now — it can be
upgraded later to a proper NLU/intent classifier without changing
processor.py's interface.
"""

from assistant.skills import time_skill, open_app_skill

INTENTS = [
    {
        "keywords": ["time", "clock"],
        "skill": time_skill,
    },
    {
        "keywords": ["open"],
        "skill": open_app_skill,
    },
]