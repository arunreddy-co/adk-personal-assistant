from typing import Optional


def extract_memory(text: str) -> Optional[dict]:
    """
    Extract a memory candidate from text.

    Returns:
        {
            "memory_type": str,
            "key": str,
            "value": str
        }

    or None.
    """

    text = text.strip()
    text_lower = text.lower()

    # Favorite editor

    if "favorite editor" in text_lower:

        parts = text.split(" is ")

        if len(parts) == 2:
            return {
                "memory_type": "user",
                "key": "favorite_editor",
                "value": parts[1].strip()
            }

    # Favorite language

    if "favorite language" in text_lower:

        parts = text.split(" is ")

        if len(parts) == 2:
            return {
                "memory_type": "user",
                "key": "favorite_language",
                "value": parts[1].strip()
            }

    # Operating system

    if text_lower.startswith("i use "):

        value = text[6:].strip()

        return {
            "memory_type": "user",
            "key": "operating_system",
            "value": value
        }

    # Current project phase

    if "current project phase" in text_lower:

        parts = text.split(" is ")

        if len(parts) == 2:
            return {
                "memory_type": "project",
                "key": "current_phase",
                "value": parts[1].strip()
            }

    return None
