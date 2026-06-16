from personal_assistant.memory.memory_manager import (
    save_user_fact,
    get_user_fact,
    save_project_fact,
    get_project_fact,
    list_user_facts,
    list_project_facts
)

from personal_assistant.tools.tool_base import safe_tool


@safe_tool
def remember_user_fact(
    key: str,
    value: str
):
    """
    Save a user fact for long-term memory.

    Example:
    favorite editor = VS Code
    favorite language = Python
    """

    save_user_fact(
        key,
        value
    )

    return f"Saved user fact: {key}"


@safe_tool
def get_user_fact_memory(
    key: str
):
    """
    Retrieve a previously saved user fact.
    """

    return get_user_fact(key)

@safe_tool
def list_user_memories():
    """
    List all stored user memories.
    """

    return list_user_facts()

@safe_tool
def remember_project_fact(
    key: str,
    value: str
):
    """
    Save project-related information.

    Example:
    current_phase = Memory Layer
    project_name = ADK Personal Assistant
    """

    save_project_fact(
        key,
        value
    )

    return f"Saved project fact: {key}"


@safe_tool
def get_project_fact_memory(
    key: str
):
    """
    Retrieve previously saved project information.
    """

    return get_project_fact(key)

@safe_tool
def list_project_memories():
    """
    List all stored project memories.
    """

    return list_project_facts()
