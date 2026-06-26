from personal_assistant.memory.episode_store import (
    save_episode,
    list_episodes
)

print(
    "\n=== SAVING TEST EPISODE ==="
)

save_episode(
    summary=(
        "Implemented merge memory"
    ),
    importance="high",
    memory_type="project",
    reason=(
        "Represents a meaningful "
        "project milestone"
    )
)

print(
    "\n=== EPISODES ==="
)

episodes = list_episodes()

for episode in episodes:

    print(
        episode
    )
