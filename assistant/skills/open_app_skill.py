"""Skill: open a Windows application."""

import subprocess

# Uses the shell's "start" command, which resolves apps the same way
# the Windows Run dialog does — works for exe names on PATH, the
# App Paths registry, and URI schemes like ms-settings: alike.
APP_MAP = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "vs code": "code",
    "visual studio code": "code",
    "settings": "ms-settings:",
    "camera": "microsoft.windows.camera:",
    "edge": "msedge",
    "spotify": "spotify:",
    "virtualbox": r"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe",
    "virtual box": r"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe",
}


def run(command: str) -> str:
    for app_name, target in APP_MAP.items():
        if app_name in command:
            subprocess.Popen(f'start "" "{target}"', shell=True)
            return f"Opening {app_name}."
    return "I don't know that app yet."