def log_memory_event(
    stage: str,
    message: str
):
    """
    Log memory system events.
    """

    print(
        f"[MEMORY:{stage}] {message}"
    )
