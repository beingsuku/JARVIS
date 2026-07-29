"""Skill: get current weather. Uses wttr.in — no API key required."""

import requests


def run(command: str) -> str:
    # Extract city: everything after "weather in" / "weather" if present.
    city = "auto"  # wttr.in auto-detects location by IP if no city given
    if " in " in command:
        city = command.split(" in ", 1)[1].strip()

    try:
        response = requests.get(f"https://wttr.in/{city}?format=%C+%t", timeout=5)
        return f"The weather is {response.text.strip()}."
    except requests.RequestException:
        return "I couldn't reach the weather service."