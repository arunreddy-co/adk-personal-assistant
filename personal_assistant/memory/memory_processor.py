from personal_assistant.memory.memory_classifier import (
    classify_memory_llm
)

from personal_assistant.memory.memory_adapter import (
    classifier_to_memory
)

from personal_assistant.memory.memory_action_executor import (
    execute_memory_action
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

    action_result = (
        execute_memory_action(
            memory
        )
    )

    print(
        action_result
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

    return action_result
