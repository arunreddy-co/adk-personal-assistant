from personal_assistant.tools.memory_tool import (
    remember,
    recall
)


remember(
    "user",
    "editor",
    "VS Code"
)

print(
    recall(
        "user",
        "editor"
    )
)
