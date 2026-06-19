from personal_assistant.memory.memory_retrieval_service import (
    retrieve_relevant_memory
)

tests = [

    "What is my favorite editor?",

    "What am I learning?",

    "Where do I live?",

    "What project am I working on?",

    "What do you know about me?"

]

for question in tests:

    print("\n" + "=" * 50)

    print(question)

    result = retrieve_relevant_memory(
        question
    )

    print(result)
