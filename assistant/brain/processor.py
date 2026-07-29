"""
The brain: routes transcribed text to the right skill.

process() is the ONLY function main.py needs to call. Everything
about how routing works is hidden behind this function, so we can
swap keyword-matching for a real NLU model later without touching
main.py at all.
"""

from assistant.brain.intents import INTENTS


def process(command: str) -> str:
    command = command.lower()

    for intent in INTENTS:
        if any(keyword in command for keyword in intent["keywords"]):
            try:
                return intent["skill"].run(command)
            except Exception as e:
                print(f"[Brain] Skill error: {e}")
                return "Sorry, something went wrong running that."

    return f"I heard: {command}, but I don't have a skill for that yet."