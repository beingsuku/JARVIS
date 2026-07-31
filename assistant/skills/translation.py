"""Skill: translate spoken phrases using deep-translator (Google Translate backend)."""

import re

from deep_translator import GoogleTranslator

_PATTERN = re.compile(
    r"(?:translation|translate)(?:\s+of)?\s+(.+?)\s+(?:to|into)\s+(.+)"
)


def _parse(command: str):
    """Returns (text_to_translate, target_language) or (None, None) if no match."""
    match = _PATTERN.search(command.lower())
    if not match:
        return None, None
    text, target_lang = match.groups()
    return text.strip(), target_lang.strip()


def run(command: str) -> str:
    text, target_lang = _parse(command)

    if not text or not target_lang:
        return "Say it like: translate hello to spanish."

    try:
        translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
    except Exception:
        return f"I don't know how to translate into '{target_lang}'."

    if not translated:
        return "I couldn't translate that."

    return f"In {target_lang}, '{text}' is: {translated}"