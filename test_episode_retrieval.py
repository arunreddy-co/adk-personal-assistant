from personal_assistant.memory.memory_retrieval_service import (
    retrieve_relevant_memory
)

QUESTIONS = [

    "What milestones have I completed?",

    "What project work have I done recently?",

    "What important decisions have I made?"
]

for question in QUESTIONS:

    print(
        "\n" + "=" * 80
    )

    print(
        "QUESTION:"
    )

    print(
        question
    )

    result = (
        retrieve_relevant_memory(
            question
        )
    )

    print(
        "\nRESULT:"
    )

    print(
        result
    )
