from personal_assistant.memory.memory_hook import (
    process_user_message
)

print("\n===== TEST 1 =====")
print(
    process_user_message(
        "My favorite editor is VS Code"
    )
)

print("\n===== TEST 2 =====")
print(
    process_user_message(
        "My favorite language is Python"
    )
)

print("\n===== TEST 3 =====")
print(
    process_user_message(
        "I use Ubuntu 24.04"
    )
)

print("\n===== TEST 4 =====")
print(
    process_user_message(
        "Hello there"
    )
)

print("\n===== TEST 5 =====")
print(
    process_user_message(
        "VS Code is a great editor"
    )
)
