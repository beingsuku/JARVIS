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
    yt_search,
    search,
    website,
    dictionary,
    translation,
    sys_info,
    clipboard,
    reminder,
    calculator,
    brightness,
    screenshot,
    recycle_bin,
    restart_app,
    power_skill,
    spotify_control
)

INTENTS = [
    {"keywords": ["time", "clock"], "skill": time_skill},
    {"keywords": ["close"], "skill": close_app},
    {"keywords": ["open"], "skill": open_app_skill},
    {"keywords": ["volume", "mute"], "skill": volume_skill},
    {"keywords": ["weather"], "skill": weather_skill},
    {"keywords": ["joke"], "skill": joke_skill},
    {"keywords": ["on youtube", "search youtube", "youtube search"], "skill": yt_search},
    {"keywords": ["search"], "skill": search},
    {"keywords": ["youtube", "github", "gmail", "website"], "skill": website},
    {"keywords": ["define", "dictionary", "meaning of"], "skill": dictionary},
    {"keywords": ["translate", "translation"], "skill": translation},
    {"keywords": ["system", "cpu", "ram", "battery"], "skill": sys_info},
    {"keywords": ["clipboard"], "skill": clipboard},
    {"keywords": ["remind"], "skill": reminder},
    {"keywords": ["calculate", "math"], "skill": calculator},
    {"keywords": ["brightness"], "skill": brightness},
    {"keywords": ["screenshot"], "skill": screenshot},
    {"keywords": ["lock", "sleep", "restart pc", "restart computer", "shutdown", "shut down"], "skill": power_skill},
    {"keywords": ["clear","bin"], "skill": recycle_bin},
    {"keywords": ["restart app"], "skill": restart_app},
    {"keywords": ["play","skip","pause","play next track"], "skill": spotify_control}
]