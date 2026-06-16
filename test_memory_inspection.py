from personal_assistant.tools.memory_tool import (
    list_user_memories,
    list_project_memories
)

print("===== USER MEMORIES =====")
print(
    list_user_memories()
)

print()

print("===== PROJECT MEMORIES =====")
print(
    list_project_memories()
)
