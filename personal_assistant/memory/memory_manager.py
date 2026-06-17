from .memory_normalizer import normalize_key

from .memory_types import (
    USER_PROFILE,
    PROJECT_MEMORY
)
from .memory_store import (
    set_memory,
    get_memory,
    list_memories,
    delete_memory
)

#User Methods
def save_user_fact(key: str, value: str):

    key = normalize_key(key)

    set_memory(
        USER_PROFILE,
        key,
        value
    )


def get_user_fact(key: str):

    key = normalize_key(key)

    return get_memory(
        USER_PROFILE,
        key
    )


def list_user_facts():
    return list_memories(
        "user_profile"
    )

#Project Methods
def save_project_fact(key: str, value: str):

    key = normalize_key(key)

    set_memory(
        PROJECT_MEMORY,
        key,
        value
    )


def get_project_fact(key: str):

    key = normalize_key(key)

    return get_memory(
        PROJECT_MEMORY,
        key
    )


def list_project_facts():
    return list_memories(
        "project_memory"
    )

def get_all_user_memories():

    return list_memories(
        USER_PROFILE
    )


def get_all_project_memories():

    return list_memories(
        PROJECT_MEMORY
    )
