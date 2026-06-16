from personal_assistant.memory.memory_processor import (
    process_memory_candidate
)

from personal_assistant.memory.memory_manager import (
    get_user_fact,
    get_project_fact
)

print(
    process_memory_candidate(
        "My favorite editor is VS Code"
    )
)

print(
    get_user_fact(
        "favorite_editor"
    )
)

print(
    process_memory_candidate(
        "The current project phase is Memory Layer"
    )
)

print(
    get_project_fact(
        "current_phase"
    )
)

print(
    process_memory_candidate(
        "Hello there"
    )
)

print(
    process_memory_candidate(
        "Python is my favorite language"
    )
)

print(
    process_memory_candidate(
        "I use Ubuntu 24.04"
    )
)
