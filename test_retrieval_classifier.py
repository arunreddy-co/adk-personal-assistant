from personal_assistant.memory.memory_retrieval_classifier import (
    classify_retrieval
)

tests = [

    "What is my favorite editor?",

    "What am I learning?",

    "Where do I live?",

    "What do you know about me?",

    "What project am I working on?"

]

for question in tests:

    print("\n" + "=" * 50)

    print(question)

    result = classify_retrieval(
        question
    )

    print(result)
