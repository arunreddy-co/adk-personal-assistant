from personal_assistant.memory.memory_ranker import (
    rank_memories
)

memories = [

    "favorite_browser = Firefox",

    "favorite_database = PostgreSQL",

    "favorite_editor = Cursor",

    "favorite_language = Python",

    "learning_topic = Rust",

    "location = Hyderabad",

    "operating_system = Ubuntu",

    "user_status = student"
]

questions = [

    "What is my favorite editor?",

    "What am I learning?",

    "Where do I live?",

    "What operating system do I use?"
]

for question in questions:

    print("\n" + "=" * 50)

    print(question)

    result = rank_memories(
        question,
        memories
    )

    print(result)
