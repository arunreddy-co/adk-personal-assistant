ALLOWED_IMPORTANCE = {
    "MEDIUM",
    "HIGH",
    "CRITICAL"
}


def should_store_episode(
    episode: dict
):
    if not episode.get(
        "store_episode"
    ):
        return False

    importance = episode.get(
        "importance"
    )

    return (
        importance
        in
        ALLOWED_IMPORTANCE
    )
