from personal_assistant.memory.memory_normalizer import (
    normalize_key
)

print(
    normalize_key(
        "favorite editor"
    )
)

print(
    normalize_key(
        "Favorite Editor"
    )
)

print(
    normalize_key(
        "favorite_editor"
    )
)

print(
    normalize_key(
        " operating system "
    )
)
