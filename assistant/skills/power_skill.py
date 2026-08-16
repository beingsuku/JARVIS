"""Skill: system power actions — lock, sleep, restart, shutdown.

Lock executes immediately (low risk, fully reversible).
Sleep/Restart/Shutdown require spoken confirmation first, since they
interrupt or end the session and a misheard command would be costly.
"""

import ctypes
import os

from assistant.listener import listen
from assistant.speaker import speak


def _confirm(action_description: str) -> bool:
    speak(f"Are you sure you want to {action_description}? Say yes to confirm.")
    response = listen()
    return "yes" in response


def _lock() -> str:
    try:
        ctypes.windll.user32.LockWorkStation()
    except Exception:
        return "Something went wrong locking the PC."
    return "Locking the PC."


def _sleep() -> str:
    if not _confirm("put the PC to sleep"):
        return "Okay, cancelling."
    try:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    except Exception:
        return "Something went wrong putting the PC to sleep."
    return "Going to sleep."


def _restart() -> str:
    if not _confirm("restart the computer"):
        return "Okay, cancelling."
    try:
        os.system("shutdown /r /t 0")
    except Exception:
        return "Something went wrong restarting the PC."
    return "Restarting the computer."


def _shutdown() -> str:
    if not _confirm("shut down the computer"):
        return "Okay, cancelling."
    try:
        os.system("shutdown /s /t 0")
    except Exception:
        return "Something went wrong shutting down the PC."
    return "Shutting down."


def run(command: str) -> str:
    command = command.lower()

    if "lock" in command:
        return _lock()
    if "sleep" in command:
        return _sleep()
    if "restart" in command:
        return _restart()
    if "shutdown" in command or "shut down" in command:
        return _shutdown()

    return "I'm not sure which power action you meant."