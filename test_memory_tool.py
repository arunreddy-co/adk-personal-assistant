from personal_assistant.tools.memory_tool import (
    remember,
    recall
)

print(
    remember(
        "user",
        "editor",
        "VS Code"
    )
)

print(
    recall(
        "user",
        "editor"
    )
)
