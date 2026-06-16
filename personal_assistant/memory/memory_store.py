from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "assistant.db"


def initialize_db():
    conn = sqlite3.connect(DB_PATH)

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

    conn.commit()
    conn.close()

    print("Database initialized.")

def set_memory(memory_type: str, key: str, value: str):
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
    """,
    (memory_type, key, value))

    conn.commit()
    conn.close()

def get_memory(memory_type: str, key: str):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.execute("""
    SELECT value
    FROM memories
    WHERE memory_type = ?
      AND key = ?
    """, (memory_type, key))

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None

def list_memories(memory_type: str | None = None):
    conn = sqlite3.connect(DB_PATH)

    if memory_type:
        cursor = conn.execute("""
        SELECT memory_type, key, value
        FROM memories
        WHERE memory_type = ?
        ORDER BY key
        """, (memory_type,))
    else:
        cursor = conn.execute("""
        SELECT memory_type, key, value
        FROM memories
        ORDER BY memory_type, key
        """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def delete_memory(memory_type: str, key: str):
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
    DELETE FROM memories
    WHERE memory_type = ?
      AND key = ?
    """, (memory_type, key))

    conn.commit()
    conn.close()
