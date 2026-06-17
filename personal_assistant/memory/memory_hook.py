from personal_assistant.memory.memory_processor import (
    process_memory_candidate
)


def process_user_message(
    message: str
):
    """
    Entry point for automatic memory capture.
    """

    return process_memory_candidate(
        message
    )
