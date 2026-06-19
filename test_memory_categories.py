from personal_assistant.memory.memory_manager import (
    get_all_user_memories,
    get_all_project_memories
)

print("\nUser Categories\n")

for row in get_all_user_memories():

    print(row[1])

print("\nProject Categories\n")

for row in get_all_project_memories():

    print(row[1])
