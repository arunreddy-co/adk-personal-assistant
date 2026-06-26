from personal_assistant.memory.episode_classifier import (
    classify_episode
)

TEST_MESSAGES = [

    "I finished implementing merge memory.",

    "I spent three hours debugging retrieval.",

    "Hello there.",

    "I decided to build an AI startup.",

    "I switched from Cursor to Vim.",

    "Today I completed the reflection system.",

    "I am learning Rust."
]

for message in TEST_MESSAGES:

    print("\n" + "=" * 80)
    print("MESSAGE:")
    print(message)

    result = classify_episode(
        message
    )

    print("\nRESULT:")
    print(result)
