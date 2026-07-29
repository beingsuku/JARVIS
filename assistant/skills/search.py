"""Skill: search the web via Google (opens in default browser)."""

import webbrowser


def run(command: str) -> str:
    query = command
    for trigger in ["search for", "search"]:
        if trigger in query:
            query = query.split(trigger, 1)[1].strip()
            break

    if not query:
        return "What do you want me to search for?"

    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Searching for {query}."