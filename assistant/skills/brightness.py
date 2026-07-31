"""Skill: control screen brightness (relative up/down, or set to a specific percent)."""

import re

import screen_brightness_control as sbc

_STEP = 20  # percent change for up/down commands


def _extract_target_percent(command: str):
    match = re.search(r"(\d{1,3})\s*(?:percent|%)?", command)
    if match:
        return max(0, min(100, int(match.group(1))))
    return None


def run(command: str) -> str:
    command = command.lower()

    try:
        current = sbc.get_brightness(display=0)[0]
    except Exception:
        return "I couldn't read the current brightness. Your display may not support this."

    try:
        if "up" in command:
            new_level = min(100, current + _STEP)
        elif "down" in command:
            new_level = max(0, current - _STEP)
        else:
            target = _extract_target_percent(command)
            if target is None:
                return "Say a percentage, or say brightness up or down."
            new_level = target

        sbc.set_brightness(new_level)
    except Exception:
        return "Something went wrong changing the brightness."

    return f"Brightness set to {new_level} percent."