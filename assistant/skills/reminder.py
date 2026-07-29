"""Skill: set a blocking reminder (Jarvis waits, then speaks the reminder)."""

import re
import time

from assistant.speaker import speak

UNIT_SECONDS = {
    "second": 1, "seconds": 1,
    "minute": 60, "minutes": 60,
    "hour": 3600, "hours": 3600,
}


def run(command: str) -> str:
    match = re.search(r"in (\d+) (second|seconds|minute|minutes|hour|hours)", command)
    if not match:
        return "Say something like: remind me in 5 minutes to check the oven."

    amount = int(match.group(1))
    unit = match.group(2)
    seconds = amount * UNIT_SECONDS[unit]

    message = ""
    if " to " in command:
        message = command.split(" to ", 1)[1].strip()

    speak(f"Okay, reminding you in {amount} {unit}.")
    time.sleep(seconds)
    speak(f"Reminder: {message}" if message else "Reminder: time's up.")

    return "Done."