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

from personal_assistant.memory.memory_kind_classifier import (
    classify_memory_kind
)

from personal_assistant.memory.episode_processor import (
    process_episode_candidate
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

def process_memory_message(
    text: str
):
    """
    Main memory entry point.

    Routes messages to the
    correct memory system.
    """

    kind_result = (
        classify_memory_kind(
            text
        )
    )

    memory_kind = (
        kind_result.get(
            "memory_kind"
        )
    )

    print(
        f"\nMEMORY KIND: "
        f"{memory_kind}"
    )

    if memory_kind == "IGNORE":

        return (
            "Memory ignored"
        )

    if memory_kind == "SEMANTIC":

        return (
            process_memory_candidate(
                text
            )
        )

    if memory_kind == "EPISODE":

        return (
            process_episode_candidate(
                text
            )
        )

    if memory_kind == "BOTH":

        semantic_result = (
            process_memory_candidate(
                text
            )
        )

        episode_result = (
            process_episode_candidate(
                text
            )
        )

        return {

            "semantic":
                semantic_result,

            "episode":
                episode_result
        }

    return (
        "Unknown memory type"
    )
