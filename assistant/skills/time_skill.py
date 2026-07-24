"""Skill: tell the current time."""

from datetime import datetime


def run(command: str) -> str:
    now = datetime.now().strftime("%I:%M %p")
    return f"It's {now}."