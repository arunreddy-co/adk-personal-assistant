from personal_assistant.memory.memory_manager import (
    save_user_fact,
    get_user_fact
)

save_user_fact(
    "Favorite Editor",
    "VS Code"
)

print(
    get_user_fact(
        "favorite editor"
    )
)

print(
    get_user_fact(
        "favorite_editor"
    )
)

print(
    process_memory_candidate(
        "My favorite language is Python"
    )
)

print(
    process_memory_candidate(
        "I use Ubuntu 24.04"
    )
)
