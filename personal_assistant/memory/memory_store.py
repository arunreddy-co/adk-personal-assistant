from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "assistant.db"


def initialize_db():

    conn = sqlite3.connect(DB_PATH)

    #
    # Memories Table
    #

    conn.execute("""
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        memory_type TEXT NOT NULL,

        key TEXT NOT NULL,

        value TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        UNIQUE(memory_type, key)
    )
    """)

    #
    # Reflections Table
    #

    conn.execute("""
    CREATE TABLE IF NOT EXISTS reflections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        reflection TEXT UNIQUE NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    #
    # Episodes Table
    #

    conn.execute("""
    CREATE TABLE IF NOT EXISTS episodes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        summary TEXT NOT NULL,

        importance TEXT NOT NULL,

        memory_type TEXT NOT NULL,

        reason TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("Database initialized.")


def set_memory(
    memory_type: str,
    key: str,
    value: str
):
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
    INSERT INTO memories (
        memory_type,
        key,
        value
    )
    VALUES (?, ?, ?)

    ON CONFLICT(memory_type, key)
    DO UPDATE SET
        value = excluded.value,
        updated_at = CURRENT_TIMESTAMP
    """, (
        memory_type,
        key,
        value
    ))

    conn.commit()
    conn.close()


def get_memory(
    memory_type: str,
    key: str
):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.execute("""
    SELECT value
    FROM memories
    WHERE memory_type = ?
      AND key = ?
    """, (
        memory_type,
        key
    ))

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None


def list_memories(
    memory_type: str | None = None
):
    conn = sqlite3.connect(DB_PATH)

    if memory_type:

        cursor = conn.execute("""
        SELECT
            memory_type,
            key,
            value
        FROM memories
        WHERE memory_type = ?
        ORDER BY key
        """, (
            memory_type,
        ))

    else:

        cursor = conn.execute("""
        SELECT
            memory_type,
            key,
            value
        FROM memories
        ORDER BY memory_type, key
        """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_memory(
    memory_type: str,
    key: str
):
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
    DELETE FROM memories
    WHERE memory_type = ?
      AND key = ?
    """, (
        memory_type,
        key
    ))

    conn.commit()
    conn.close()


def merge_memory(
    memory_type: str,
    key: str,
    value: str
):
    """
    Merge new value into an existing memory.

    Example:

    Existing:
        Python

    New:
        JavaScript

    Result:
        Python, JavaScript
    """

    existing = get_memory(
        memory_type,
        key
    )

    #
    # No existing memory
    #

    if not existing:

        set_memory(
            memory_type,
            key,
            value
        )

        return

    #
    # Preserve insertion order
    #

    existing_parts = [

        item.strip()

        for item in existing.split(",")

        if item.strip()
    ]

    for item in value.split(","):

        item = item.strip()

        if (
            item
            and
            item not in existing_parts
        ):
            existing_parts.append(
                item
            )

    merged_value = ", ".join(
        existing_parts
    )

    set_memory(
        memory_type,
        key,
        merged_value
    )


#
# Episode Functions
#

def save_episode(
    summary: str,
    importance: str,
    memory_type: str,
    reason: str
):
    conn = sqlite3.connect(DB_PATH)

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

    conn = sqlite3.connect(DB_PATH)

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
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
    DELETE FROM episodes
    WHERE id = ?
    """, (
        episode_id,
    ))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_db()
