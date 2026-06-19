from personal_assistant.memory.memory_manager import (
    get_all_user_memories,
    get_all_project_memories
)

from personal_assistant.memory.reflection_manager import (
    list_reflections
)


def retrieve_domain_memories(
    memory_types: list[str]
):
    """
    Retrieve memories belonging
    to the requested domains.
    """

    memories = []

    if "PROFILE" in memory_types:

        user_memories = (
            get_all_user_memories()
        )

        for _, key, value in user_memories:

            memories.append(
                f"{key} = {value}"
            )

    if "PROJECT" in memory_types:

        project_memories = (
            get_all_project_memories()
        )

        for _, key, value in project_memories:

            memories.append(
                f"{key} = {value}"
            )

    if "REFLECTION" in memory_types:

        reflections = (
            list_reflections()
        )

        for reflection in reflections:

            memories.append(
                f"reflection = {reflection}"
            )

    return memories
