from personal_assistant.memory.memory_extractor import (
    extract_memory
)

print(
    extract_memory(
        "My favorite editor is VS Code"
    )
)

print(
    extract_memory(
        "My favorite language is Python"
    )
)

print(
    extract_memory(
        "I use Ubuntu 24.04"
    )
)

print(
    extract_memory(
        "The current project phase is Memory Layer"
    )
)
