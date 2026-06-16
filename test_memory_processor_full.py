from personal_assistant.memory.memory_processor import (
    process_memory_candidate
)

print(
    process_memory_candidate(
        "VS Code is a great editor"
    )
)

print(
    process_memory_candidate(
        "Python is awesome"
    )
)

print(
    process_memory_candidate(
        "The weather is nice today"
    )
)
