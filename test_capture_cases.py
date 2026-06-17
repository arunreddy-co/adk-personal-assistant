from personal_assistant.memory.memory_policy import (
    classify_memory
)

from personal_assistant.memory.memory_extractor import (
    extract_memory
)

cases = [
    "What is my favorite editor?",
    "My favorite editor is VS Code",
    "My favourite editor is VS Code",
    "Favorite editor is VS Code",
    "My favorite database is PostgreSQL",
    "I use Ubuntu 24.04",
    "I am learning Rust",
    "The weather is nice",
    "The current project phase is Memory Layer"
]

for case in cases:

    print("\n" + "=" * 50)
    print(f"INPUT: {case}")

    classification = classify_memory(case)

    print(
        f"CLASSIFICATION: {classification}"
    )

    extracted = extract_memory(case)

    print(
        f"EXTRACTION: {extracted}"
    )
