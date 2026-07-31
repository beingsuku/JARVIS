"""Skill: lock the Windows PC."""

import ctypes


def run(command: str) -> str:
    try:
        ctypes.windll.user32.LockWorkStation()
    except Exception:
        return "Something went wrong locking the PC."

    return "Locking the PC."