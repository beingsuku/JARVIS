"""Skill: take a screenshot and save it with a timestamped filename."""

import os
from datetime import datetime

from PIL import ImageGrab

_SAVE_DIR = r"C:\Users\saksh\OneDrive\Pictures\Screenshots"


def run(command: str) -> str:
    os.makedirs(_SAVE_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(_SAVE_DIR, filename)

    try:
        screenshot = ImageGrab.grab()
        screenshot.save(filepath)
    except Exception:
        return "Something went wrong taking the screenshot."

    return f"Screenshot saved."