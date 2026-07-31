"""Skill: look up word definitions using the free dictionaryapi.dev API."""

import re

import requests

_TRIGGER_PHRASES = ["meaning of", "define", "dictionary"]
_FILLER_WORDS = {"the", "of", "a", "an", "word", "please"}

_API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"


def _extract_word(command: str) -> str:
    text = command.lower()

    for phrase in _TRIGGER_PHRASES:
        text = text.replace(phrase, " ")

    tokens = [t for t in text.split() if t not in _FILLER_WORDS]
    return tokens[-1] if tokens else ""


def run(command: str) -> str:
    word = _extract_word(command)

    if not word:
        return "I didn't catch which word you want defined."

    try:
        response = requests.get(_API_URL.format(word=word), timeout=5)
    except requests.RequestException:
        return "I couldn't reach the dictionary service right now."

    if response.status_code == 404:
        return f"I couldn't find a definition for '{word}'."

    if response.status_code != 200:
        return "Something went wrong looking that up."

    try:
        data = response.json()
        first_entry = data[0]
        part_of_speech = first_entry["meanings"][0]["partOfSpeech"]
        definition = first_entry["meanings"][0]["definitions"][0]["definition"]
    except (KeyError, IndexError, ValueError):
        return f"I found '{word}' but couldn't parse its definition."

    return f"{word}, {part_of_speech}: {definition}"