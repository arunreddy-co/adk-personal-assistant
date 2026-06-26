from personal_assistant.memory.memory_processor import (
    process_memory_message
)

TEST_MESSAGES = [

    "I am learning Rust.",

    "I completed merge memory.",

    "I decided to build an AI startup.",

    "Hello there."
]

for message in TEST_MESSAGES:

    print(
        "\n" + "=" * 80
    )

    print(
        "MESSAGE:"
    )

    print(
        message
    )

    result = (
        process_memory_message(
            message
        )
    )

    print(
        "\nRESULT:"
    )

    print(
        result
    )
