"""Skill: open specific websites and bring the browser to the foreground."""

import time
import webbrowser
import pygetwindow as gw

# (url, a snippet of text expected in the browser tab's window title)
SITE_MAP = {
    "youtube": ("https://www.youtube.com", "YouTube"),
    "github": ("https://www.github.com", "GitHub"),
    "gmail": ("https://mail.google.com", "Gmail"),
}


def _bring_to_front(title_hint: str) -> None:
    time.sleep(1.5)  # give the browser a moment to open/switch tab
    for window in gw.getWindowsWithTitle(title_hint):
        try:
            window.minimize()
            window.restore()
            window.activate()
        except Exception:
            pass


def run(command: str) -> str:
    for site_name, (url, title_hint) in SITE_MAP.items():
        if site_name in command:
            webbrowser.open(url)
            _bring_to_front(title_hint)
            return f"Opening {site_name}."
    return "I don't know that website yet."