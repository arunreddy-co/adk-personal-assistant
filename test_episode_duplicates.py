from personal_assistant.memory.episode_processor import (
    process_episode_candidate
)

print("\n=== FIRST RUN ===")

result = process_episode_candidate(
    "I completed merge memory."
)

print(result)

print("\n=== SECOND RUN ===")

result = process_episode_candidate(
    "I completed merge memory."
)

print(result)
