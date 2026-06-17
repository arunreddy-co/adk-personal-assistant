"""
Memory Policy V1

Purpose:
Decide whether information should be stored as memory.

Returns:
- "user"
- "project"
- "ignore"
"""


USER_KEYWORDS = [
    "favorite",
    "prefer",
    "preference",
    "editor",
    "language",
    "ubuntu",
    "python",
    "name"
]

PROJECT_KEYWORDS = [
    "project",
    "phase",
    "milestone",
    "tool",
    "feature",
    "memory layer",
    "adk",
    "assistant"
]


def classify_memory(text: str) -> str:
    """
    Classify text as:

    - user
    - project
    - ignore
    """
    text = text.strip()

    if text.endswith("?"):
        return "ignore"

    text = text.lower()

    for keyword in USER_KEYWORDS:
        if keyword in text:
            return "user"

    for keyword in PROJECT_KEYWORDS:
        if keyword in text:
            return "project"

    return "ignore"
