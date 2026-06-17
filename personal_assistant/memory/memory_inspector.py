from personal_assistant.memory.memory_manager import (
    get_all_user_memories,
    get_all_project_memories
)


def build_memory_summary():
    """
    Build a memory summary
    for prompt injection.
    """

    user_memories = (
        get_all_user_memories()
    )

    project_memories = (
        get_all_project_memories()
    )

    lines = []

    if user_memories:

        lines.append(
            "User Memories:"
        )

        for _, key, value in user_memories:

            lines.append(
                f"- {key}: {value}"
            )

    if project_memories:

        lines.append("")
        lines.append(
            "Project Memories:"
        )

        for _, key, value in project_memories:

            lines.append(
                f"- {key}: {value}"
            )

    return "\n".join(lines)
