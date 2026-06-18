def classifier_to_memory(
    result: dict
):

    if not result:
        return None

    action = result.get(
        "action"
    )

    if action == "IGNORE":
        return None

    return {

        "action":
            action,

        "memory_type":
            result["memory_type"],

        "key":
            result["category"],

        "value":
            result["value"]
    }
