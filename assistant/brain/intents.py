"""
Intent definitions: maps trigger keywords to a skill module.
This is deliberately simple (keyword matching) for now — it can be
upgraded later to a proper NLU/intent classifier without changing
processor.py's interface.
"""
from assistant.skills import (
    time_skill,
    open_app_skill,
    close_app,
    volume_skill,
    weather_skill,
    joke_skill,
    search,
    website,
    sys_info,
    clipboard,
    reminder,
)

INTENTS = [
    {"keywords": ["time", "clock"], "skill": time_skill},
    {"keywords": ["close"], "skill": close_app},
    {"keywords": ["open"], "skill": open_app_skill},
    {"keywords": ["volume", "mute"], "skill": volume_skill},
    {"keywords": ["weather"], "skill": weather_skill},
    {"keywords": ["joke"], "skill": joke_skill},
    {"keywords": ["search"], "skill": search},
    {"keywords": ["youtube", "github", "gmail", "website"], "skill": website},
    {"keywords": ["system", "cpu", "ram", "battery"], "skill": sys_info},
    {"keywords": ["clipboard"], "skill": clipboard},
    {"keywords": ["remind"], "skill": reminder},
]