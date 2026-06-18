from personal_assistant.memory.memory_classifier import (
    classify_memory_llm
)

from personal_assistant.memory.memory_adapter import (
    classifier_to_memory
)

from personal_assistant.memory.memory_manager import (
    save_user_fact,
    save_project_fact
)

from personal_assistant.memory.memory_logger import (
    log_memory_event
)

from personal_assistant.memory.reflection_trigger import (
    should_generate_reflection
)

from personal_assistant.memory.memory_reflector import (
    generate_reflections
)


def process_memory_candidate(
    text: str
):

    log_memory_event(
        "INPUT",
        text
    )

    result = classify_memory_llm(
        text
    )

    log_memory_event(
        "LLM_RESULT",
        str(result)
    )

    memory = (
        classifier_to_memory(
            result
        )
    )

    if memory is None:

        log_memory_event(
            "IGNORE",
            "Memory ignored"
        )

        return "Ignored"

    if memory["memory_type"] == "user":

        save_user_fact(
            memory["key"],
            memory["value"]
        )

        log_memory_event(
            "SAVED",
            f"user:{memory['key']}"
        )

        if should_generate_reflection():

            print(
                "\n===== REFLECTION TRIGGERED ====="
            )

            reflections = (
                generate_reflections()
            )

            print(
                reflections
            )

        return (
            f"Saved user memory: "
            f"{memory['key']}"
        )

    if memory["memory_type"] == "project":

        save_project_fact(
            memory["key"],
            memory["value"]
        )

        log_memory_event(
            "SAVED",
            f"project:{memory['key']}"
        )

        if should_generate_reflection():

            print(
                "\n===== REFLECTION TRIGGERED ====="
            )

            reflections = (
                generate_reflections()
            )

            print(
                reflections
            )

        return (
            f"Saved project memory: "
            f"{memory['key']}"
        )

    return "Unsupported memory type"
