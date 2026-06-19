from personal_assistant.memory.memory_retriever import (
    retrieve_relevant_memory
)

tests = [

    "What project am I working on?",

    "What do you know about me?"

]

for question in tests:

    print("\n" + "=" * 50)

    print(question)

    memories = (
        retrieve_relevant_memory(
            question
        )
    )

    for memory in memories:

        print(memory)
