from personal_assistant.memory.memory_domain_classifier import (
    classify_memory_domains
)

from personal_assistant.memory.memory_domain_retriever import (
    retrieve_domain_memories
)

from personal_assistant.memory.memory_ranker import (
    rank_memories
)


def retrieve_relevant_memory(
    user_message: str
):
    """
    Retrieval V2

    Question
        ↓
    Domain Classifier
        ↓
    Domain Retriever
        ↓
    Memory Ranker
        ↓
    Relevant Memories
    """

    memory_types = (
        classify_memory_domains(
            user_message
        )
    )

    candidate_memories = (
        retrieve_domain_memories(
            memory_types
        )
    )

    ranked_memories = (
        rank_memories(
            user_message,
            candidate_memories
        )
    )

    return ranked_memories
