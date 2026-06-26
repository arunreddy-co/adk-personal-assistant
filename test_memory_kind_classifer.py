from personal_assistant.memory.memory_kind_classifier import (
    classify_memory_kind
)

TEST_MESSAGES = [

    "I am learning Rust.",

    "My favorite editor is Cursor.",

    "I completed merge memory.",

    "I spent three hours debugging retrieval.",

    "I decided to build an AI startup.",

    "I changed my career goal.",

    "Hello there.",

    "Thanks."
]

for message in TEST_MESSAGES:

    print("\n" + "=" * 80)

    print("MESSAGE:")
    print(message)

    result = classify_memory_kind(
        message
    )

    print("\nRESULT:")
    print(result)
