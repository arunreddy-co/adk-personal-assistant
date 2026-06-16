from personal_assistant.memory.memory_policy import (
    classify_memory
)

from personal_assistant.memory.memory_extractor import (
    extract_memory
)

from personal_assistant.memory.memory_manager import (
    save_user_fact,
    save_project_fact
)

from personal_assistant.memory.memory_logger import (
    log_memory_event
)

def process_memory_candidate(text: str):

    log_memory_event(
        "INPUT",
        text
    )

    memory_class = classify_memory(text)

    log_memory_event(
        "CLASSIFICATION",
        memory_class
    )

    if memory_class == "ignore":

        log_memory_event(
            "IGNORE",
            "Memory ignored"
        )

        return "Ignored"

    memory = extract_memory(text)

    log_memory_event(
        "EXTRACTED",
        str(memory)
    )

    if memory is None:

        log_memory_event(
            "FAILED",
            "No memory extracted"
        )

        return "No memory extracted"

    if memory["memory_type"] == "user":

        save_user_fact(
            memory["key"],
            memory["value"]
        )

        log_memory_event(
            "SAVED",
            f"user:{memory['key']}"
        )

        return f"Saved user memory: {memory['key']}"

    if memory["memory_type"] == "project":

        save_project_fact(
            memory["key"],
            memory["value"]
        )

        log_memory_event(
            "SAVED",
            f"project:{memory['key']}"
        )

        return f"Saved project memory: {memory['key']}"

    return "Unsupported memory type"
