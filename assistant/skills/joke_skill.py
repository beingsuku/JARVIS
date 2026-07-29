"""Skill: tell a random joke. No external dependencies."""

import random

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I would tell you a UDP joke, but you might not get it.",
    "There are 10 types of people: those who understand binary and those who don't.",
]


def run(command: str) -> str:
    return random.choice(JOKES)