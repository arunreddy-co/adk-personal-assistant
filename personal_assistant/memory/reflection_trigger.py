from personal_assistant.memory.memory_manager import (
    get_all_user_memories,
    get_all_project_memories
)

REFLECTION_INTERVAL = 10


def should_generate_reflection():

    user_memories = (
        get_all_user_memories()
    )

    project_memories = (
        get_all_project_memories()
    )

    total_memories = (
        len(user_memories)
        +
        len(project_memories)
    )

    print(
        f"[MEMORY COUNT] {total_memories}"
    )

    return (
        total_memories > 0
        and
        total_memories % REFLECTION_INTERVAL == 0
    )
