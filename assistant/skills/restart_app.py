"""Skill: restart an application (close it, then reopen it).

Reuses the existing close_app and open_app_skill modules rather than
duplicating their logic — an app can only be restarted if it exists
in BOTH their APP_MAPs (needs to be closeable AND reopenable).
"""

import time

from assistant.skills import close_app, open_app_skill


def run(command: str) -> str:
    matched_app = None
    for app_name in close_app.APP_MAP:
        if app_name in command and app_name in open_app_skill.APP_MAP:
            matched_app = app_name
            break

    if not matched_app:
        return "I don't know that app, or I can't restart it."

    close_app.run(command)
    time.sleep(2)  # give Windows time to fully terminate the process before reopening
    open_app_skill.run(command)

    return f"Restarting {matched_app}."