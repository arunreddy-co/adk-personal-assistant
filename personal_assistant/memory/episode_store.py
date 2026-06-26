from personal_assistant.memory.memory_store import (
    DB_PATH
)

import sqlite3


def save_episode(
    summary: str,
    importance: str,
    memory_type: str,
    reason: str
):
    conn = sqlite3.connect(
        DB_PATH
    )

    conn.execute("""
    INSERT INTO episodes (
        summary,
        importance,
        memory_type,
        reason
    )
    VALUES (?, ?, ?, ?)
    """, (
        summary,
        importance,
        memory_type,
        reason
    ))

    conn.commit()
    conn.close()


def list_episodes():

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.execute("""
    SELECT
        id,
        summary,
        importance,
        memory_type,
        reason,
        created_at
    FROM episodes
    ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_episode(
    episode_id: int
):
    conn = sqlite3.connect(
        DB_PATH
    )

    conn.execute("""
    DELETE FROM episodes
    WHERE id = ?
    """, (
        episode_id,
    ))

    conn.commit()
    conn.close()
