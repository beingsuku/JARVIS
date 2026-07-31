"""Skill: empty the Windows recycle bin."""

import winshell


def run(command: str) -> str:
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    except Exception:
        return "Something went wrong emptying the recycle bin."

    return "Recycle bin emptied."