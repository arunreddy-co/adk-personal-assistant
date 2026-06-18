from personal_assistant.memory.memory_classifier import (
    classify_memory_llm
)

tests = [

    "My favorite editor is Vim",

    "I switched from Vim to Cursor",

    "I am learning Rust",

    "Current project phase is Memory Layer",

    "Hello there"

]

for text in tests:

    print("\n" + "=" * 50)

    print(text)

    result = classify_memory_llm(
        text
    )

    print(result)
