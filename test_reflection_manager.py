from personal_assistant.memory.reflection_manager import (
    save_reflection,
    list_reflections
)

save_reflection(
    "User prefers technical tools."
)

for reflection in list_reflections():

    print(reflection)
