from personal_assistant.memory.episode_processor import (
    process_episode_candidate
)

TEST_MESSAGES = [

    "I completed merge memory.",

    "I spent three hours debugging retrieval.",

    "Hello there.",

    "I decided to build an AI startup.",

    "I am learning Rust."
]

for message in TEST_MESSAGES:

    print("\n" + "=" * 80)

    print("MESSAGE:")
    print(message)

    result = process_episode_candidate(
        message
    )

    print("\nRESULT:")
    print(result)
