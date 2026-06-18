import sqlite3

from .memory_store import DB_PATH


def save_reflection(
    reflection: str
):

    conn = sqlite3.connect(
        DB_PATH
    )

    conn.execute(
        """
        INSERT OR IGNORE INTO reflections (
            reflection
        )
        VALUES (?)
        """,
        (reflection,)
    )

    conn.commit()

    conn.close()


def list_reflections():

    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.execute(
        """
        SELECT reflection
        FROM reflections
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        row[0]
        for row in rows
    ]
