from personal_assistant.memory.memory_classifier import (
    classify_memory_llm
)

tests = [

    "I am a student",

    "I work as a software engineer",

    "I live in Hyderabad",

    "I switched from VS Code to Vim",

    "I am learning Rust",

    "Hello there"
]

for text in tests:

    print("\n" + "=" * 50)

    print(text)

    result = classify_memory_llm(
        text
    )

    print(result)
