"""Skill: perform calculations with spoken math expressions."""

import ast
import operator
import re

from word2number import w2n

# Multi-word operator phrases checked before single words (order matters)
_PHRASE_OPERATORS = [
    ("divided by", "/"),
    ("multiplied by", "*"),
    ("added to", "+"),
    ("subtracted from", "-"),
    ("plus", "+"),
    ("minus", "-"),
    ("times", "*"),
    ("multiply", "*"),
    ("divide", "/"),
    ("add", "+"),
    ("subtract", "-"),
]
_X_MULTIPLY = re.compile(r"(?<=\d)\s*x\s*(?=\d)")

# Trigger/filler words stripped out before parsing the expression
_FILLER_WORDS = {"calculate", "math", "please", "equals", "result", "of"}

_NUMBER_WORDS = {
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty",
    "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred",
    "thousand", "point",
}

_ALLOWED_CHARS = re.compile(r"^[0-9+\-*/(). ]+$")

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _replace_phrase_operators(text: str) -> str:
    for phrase, symbol in _PHRASE_OPERATORS:
        text = text.replace(phrase, f" {symbol} ")
    return text


def _words_to_numbers(text: str) -> str:
    """Convert runs of spoken number words (e.g. 'twenty three') into digit strings."""
    tokens = text.split()
    result = []
    buffer = []

    def flush_buffer():
        if buffer:
            try:
                result.append(str(w2n.word_to_num(" ".join(buffer))))
            except ValueError:
                result.extend(buffer)  # couldn't parse, keep original words
            buffer.clear()

    for token in tokens:
        if token in _NUMBER_WORDS:
            buffer.append(token)
        else:
            flush_buffer()
            result.append(token)
    flush_buffer()

    return " ".join(result)


def _build_expression(command: str) -> str:
    text = command.lower()

    for word in _FILLER_WORDS:
        text = re.sub(rf"\b{word}\b", " ", text)

    text = _replace_phrase_operators(text)
    text = _X_MULTIPLY.sub(" * ", text)
    text = _words_to_numbers(text)

    return " ".join(text.split())  # collapse whitespace


def _eval_node(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.BinOp):
        return _OPS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    if isinstance(node, ast.UnaryOp):
        return _OPS[type(node.op)](_eval_node(node.operand))
    raise ValueError("Unsupported expression.")


def _safe_eval(expression: str):
    if not _ALLOWED_CHARS.match(expression):
        raise ValueError("Expression contains disallowed characters.")
    tree = ast.parse(expression, mode="eval")
    return _eval_node(tree.body)


def run(command: str) -> str:
    expression = _build_expression(command)

    if not expression.strip():
        return "I didn't catch a calculation in that."

    try:
        result = _safe_eval(expression)
    except ZeroDivisionError:
        return "I can't divide by zero."
    except Exception:
        return f"Sorry, I couldn't work out '{command}'."

    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return f"That's {result}."