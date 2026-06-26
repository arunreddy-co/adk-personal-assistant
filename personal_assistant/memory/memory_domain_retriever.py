from personal_assistant.memory.memory_manager import (
    get_all_user_memories,
    get_all_project_memories
)

from personal_assistant.memory.reflection_manager import (
    list_reflections
)

from personal_assistant.memory.episode_store import (
    list_episodes
)


def retrieve_domain_memories(
    memory_types: list[str]
):
    """
    Retrieve memories belonging
    to the requested domains.
    """

    memories = []

    #
    # PROFILE
    #

    if "PROFILE" in memory_types:

        user_memories = (
            get_all_user_memories()
        )

        for _, key, value in user_memories:

            memories.append(
                f"{key} = {value}"
            )

    #
    # PROJECT
    #

    if "PROJECT" in memory_types:

        project_memories = (
            get_all_project_memories()
        )

        for _, key, value in project_memories:

            memories.append(
                f"{key} = {value}"
            )

    #
    # REFLECTION
    #

    if "REFLECTION" in memory_types:

        reflections = (
            list_reflections()
        )

        for reflection in reflections:

            memories.append(
                f"reflection = {reflection}"
            )

    #
    # EPISODE
    #

    if "EPISODE" in memory_types:

        episodes = (
            list_episodes()
        )

        for (
            _,
            summary,
            importance,
            memory_type,
            reason,
            created_at
        ) in episodes:

            memories.append(
                (
                    f"episode = "
                    f"{summary}"
                )
            )

    return memories
