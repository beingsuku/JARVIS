"""Skill: close a running Windows application."""

import subprocess

APP_MAP = {
    "notepad": "notepad.exe",
    "calculator": "CalculatorApp.exe",
    "vs code": "Code.exe",
    "visual studio code": "Code.exe",
    "edge": "msedge.exe",
    "spotify": "Spotify.exe",
    "camera": "WindowsCamera.exe",
    "virtualbox": "VirtualBox.exe",
    "virtual box": "VirtualBox.exe",
}


def run(command: str) -> str:
    for app_name, executable in APP_MAP.items():
        if app_name in command:
            subprocess.run(["taskkill", "/IM", executable, "/F"], capture_output=True)
            return f"Closing {app_name}."
    return "I don't know that app yet."