def normalize_key(key: str) -> str:
    """
    Convert memory keys into a canonical format.
    """

    key = key.strip().lower()

    key = key.replace(" ", "_")

    return key
