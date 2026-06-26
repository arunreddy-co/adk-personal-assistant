from personal_assistant.memory.episode_classifier import (
    classify_episode
)

from personal_assistant.memory.episode_policy import (
    should_store_episode
)

from personal_assistant.memory.memory_store import (
    save_episode
)

from personal_assistant.memory.episode_store import (
    list_episodes
)

def episode_exists(
    summary: str
):
    """
    Prevent duplicate episodes.
    """

    episodes = list_episodes()

    for (
        _,
        existing_summary,
        _,
        _,
        _,
        _
    ) in episodes:

        if (
            existing_summary.strip().lower()
            ==
            summary.strip().lower()
        ):
            return True

    return False

def process_episode_candidate(
    text: str
):
    """
    Process a possible episode.

    Flow:

    Message
        ↓
    Episode Classifier
        ↓
    Policy
        ↓
    Storage
    """

    result = classify_episode(
        text
    )

    if not should_store_episode(
        result
    ):
        return {
            "stored": False,
            "episode": result
        }

    #
    # Duplicate Guard
    #

    if episode_exists(
        result["summary"]
    ):
        return {
            "stored": False,
            "reason": "Duplicate episode",
            "episode": result
        }

    save_episode(
        summary=result[
            "summary"
        ],

        importance=result[
            "importance"
        ],

        memory_type=result[
            "memory_type"
        ],

        reason=result[
            "reason"
        ]
    )

    return {
        "stored": True,
        "episode": result
    }
