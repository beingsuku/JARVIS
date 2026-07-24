"""Skill: open a Windows application."""

import subprocess

# Maps spoken app names to actual executable names.
# This dict will grow a lot in Stage 6 — keep it simple for now.
APP_MAP = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
}


def run(command: str) -> str:
    for app_name, executable in APP_MAP.items():
        if app_name in command:
            subprocess.Popen(executable)
            return f"Opening {app_name}."
    return "I don't know that app yet."