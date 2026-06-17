from personal_assistant.memory.memory_retriever import (
    retrieve_relevant_memory
)

tests = [

    "What is my favorite editor?",
    "What is my favourite editor?",
    "Do you remember my favorite editor?",
    "What editor do I use?",

    "What is my favorite language?",
    "What language do I like?",

    "What is my favorite database?",
    "What database do I prefer?",

    "What is my operating system?",
    "Which OS do I use?",

    "What is the current phase?",
    "What phase is the project in?",

    "What is the project name?",

    "Hello there"
]

for test in tests:

    print("\n" + "=" * 50)
    print(test)

    result = retrieve_relevant_memory(
        test
    )

    print(result)
