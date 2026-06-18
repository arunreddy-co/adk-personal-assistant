def classifier_to_memory(
    result: dict
):

    if not result:
        return None

    if not result.get(
        "remember"
    ):
        return None

    return {

        "memory_type":
            result["memory_type"],

        "key":
            result["category"],

        "value":
            result["value"]
    }
