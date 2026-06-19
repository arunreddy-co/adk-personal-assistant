from personal_assistant.memory.memory_domain_classifier import (
    classify_memory_domains
)

tests = [

    "What is my favorite editor?",

    "What am I learning?",

    "Where do I live?",

    "What project am I working on?",

    "What do you know about me?",

    "What are my goals?",

    "What happened recently?"
]

for question in tests:

    print("\n" + "=" * 50)

    print(question)

    result = classify_memory_domains(
        question
    )

    print(result)
