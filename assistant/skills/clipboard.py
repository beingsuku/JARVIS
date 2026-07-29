"""Skill: read from or copy to the clipboard."""

import pyperclip


def run(command: str) -> str:
    if "read" in command:
        content = pyperclip.paste()
        if not content:
            return "Clipboard is empty."
        return f"Clipboard says: {content}"

    if "copy" in command:
        text = command.split("copy", 1)[1].strip()
        if not text:
            return "What do you want me to copy?"
        pyperclip.copy(text)
        return "Copied to clipboard."

    return "Say clipboard read, or clipboard copy something."