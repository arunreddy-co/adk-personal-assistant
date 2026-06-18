from personal_assistant.memory.memory_processor import (
    process_memory_candidate
)

tests = [

    "My favorite editor is Vim",

    "I switched from Vim to Cursor",

    "I am learning Rust",

    "Hello there"

]

for text in tests:

    print("\n" + "=" * 50)

    print(text)

    result = process_memory_candidate(
        text
    )

    print(result)
