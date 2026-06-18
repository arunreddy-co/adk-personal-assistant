from personal_assistant.memory.memory_manager import (
    save_user_fact,
    save_project_fact
)

from personal_assistant.memory.memory_store import (
    delete_memory
)

from personal_assistant.memory.memory_logger import (
    log_memory_event
)


def execute_memory_action(
    memory: dict
):
    """
    Execute memory action.

    Supported actions:

    CREATE
    UPDATE
    MERGE
    DELETE
    IGNORE
    """

    action = memory.get(
        "action"
    )

    if action == "IGNORE":

        log_memory_event(
            "IGNORE",
            "Memory ignored"
        )

        return "Ignored"

    memory_type = memory.get(
        "memory_type"
    )

    key = memory.get(
        "key"
    )

    value = memory.get(
        "value"
    )

    if action in (
        "CREATE",
        "UPDATE",
        "MERGE"
    ):

        if memory_type == "user":

            save_user_fact(
                key,
                value
            )

            log_memory_event(
                action,
                f"user:{key}"
            )

            return (
                f"{action} user memory: "
                f"{key}"
            )

        if memory_type == "project":

            save_project_fact(
                key,
                value
            )

            log_memory_event(
                action,
                f"project:{key}"
            )

            return (
                f"{action} project memory: "
                f"{key}"
            )

    if action == "DELETE":

        memory_store_type = (
            "user_profile"
            if memory_type == "user"
            else
            "project_memory"
        )

        delete_memory(
            memory_store_type,
            key
        )

        log_memory_event(
            "DELETE",
            f"{memory_type}:{key}"
        )

        return (
            f"Deleted memory: "
            f"{key}"
        )

    return (
        f"Unsupported action: "
        f"{action}"
    )
