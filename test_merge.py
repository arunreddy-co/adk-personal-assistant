from personal_assistant.memory.memory_manager import (
    merge_user_fact,
    get_user_fact
)

print(
    "\n=== TEST 1 ==="
)

merge_user_fact(
    "learning_topic",
    "Python"
)

print(
    get_user_fact(
        "learning_topic"
    )
)

print(
    "\n=== TEST 2 ==="
)

merge_user_fact(
    "learning_topic",
    "JavaScript"
)

print(
    get_user_fact(
        "learning_topic"
    )
)

print(
    "\n=== TEST 3 ==="
)

merge_user_fact(
    "learning_topic",
    "Python"
)

print(
    get_user_fact(
        "learning_topic"
    )
)

print(
    "\n=== TEST 4 ==="
)

merge_user_fact(
    "learning_topic",
    "Rust"
)

print(
    get_user_fact(
        "learning_topic"
    )
)
