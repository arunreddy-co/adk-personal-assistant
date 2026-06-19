from personal_assistant.memory.memory_domain_retriever import (
    retrieve_domain_memories
)

tests = [

    ["PROFILE"],

    ["PROJECT"],

    ["REFLECTION"],

    ["PROFILE", "PROJECT"]

]

for memory_types in tests:

    print("\n" + "=" * 50)

    print(memory_types)

    result = retrieve_domain_memories(
        memory_types
    )

    for memory in result:

        print(memory)
