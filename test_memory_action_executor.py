from personal_assistant.memory.memory_action_executor import (
    execute_memory_action
)

tests = [

    {
        "action": "CREATE",
        "memory_type": "user",
        "key": "favorite_editor",
        "value": "Vim"
    },

    {
        "action": "UPDATE",
        "memory_type": "user",
        "key": "favorite_editor",
        "value": "Cursor"
    },

    {
        "action": "CREATE",
        "memory_type": "project",
        "key": "current_phase",
        "value": "Memory Layer"
    },

    {
        "action": "DELETE",
        "memory_type": "user",
        "key": "favorite_editor",
        "value": None
    },

    {
        "action": "IGNORE"
    }

]

for test in tests:

    print(
        execute_memory_action(
            test
        )
    )
