from personal_assistant.memory.memory_manager import (
    get_user_fact,
    get_project_fact
)


EDITOR_PATTERNS = [
    "favorite editor",
    "favourite editor",
    "editor do i use",
    "which editor",
    "what editor"
]

LANGUAGE_PATTERNS = [
    "favorite language",
    "favourite language",
    "what language",
    "language do i use",
    "language do i like"
]

DATABASE_PATTERNS = [
    "favorite database",
    "favourite database",
    "what database",
    "database do i use",
    "database do i prefer"
]

OS_PATTERNS = [
    "operating system",
    "what os",
    "which os",
    "what system do i use"
]

PROJECT_PHASE_PATTERNS = [
    "current phase",
    "project phase",
    "what phase"
]

PROJECT_NAME_PATTERNS = [
    "project name",
    "name of the project",
    "what is the project called"
]


def contains_pattern(
    text: str,
    patterns: list[str]
) -> bool:

    for pattern in patterns:

        if pattern in text:
            return True

    return False


def retrieve_relevant_memory(
    user_message: str
):
    """
    Retrieve memories relevant to
    the user's question.

    Returns:
        list[str]
    """

    text = user_message.lower()

    memories = []

    # Favorite Editor

    if contains_pattern(
        text,
        EDITOR_PATTERNS
    ):

        value = get_user_fact(
            "favorite_editor"
        )

        if value:

            memories.append(
                f"favorite_editor = {value}"
            )

    # Favorite Language

    if contains_pattern(
        text,
        LANGUAGE_PATTERNS
    ):

        value = get_user_fact(
            "favorite_language"
        )

        if value:

            memories.append(
                f"favorite_language = {value}"
            )

    # Favorite Database

    if contains_pattern(
        text,
        DATABASE_PATTERNS
    ):

        value = get_user_fact(
            "favorite_database"
        )

        if value:

            memories.append(
                f"favorite_database = {value}"
            )

    # Operating System

    if contains_pattern(
        text,
        OS_PATTERNS
    ):

        value = get_user_fact(
            "operating_system"
        )

        if value:

            memories.append(
                f"operating_system = {value}"
            )

    # Project Phase

    if contains_pattern(
        text,
        PROJECT_PHASE_PATTERNS
    ):

        value = get_project_fact(
            "current_phase"
        )

        if value:

            memories.append(
                f"current_phase = {value}"
            )

    # Project Name

    if contains_pattern(
        text,
        PROJECT_NAME_PATTERNS
    ):

        value = get_project_fact(
            "project_name"
        )

        if value:

            memories.append(
                f"project_name = {value}"
            )

    return memories
