import json
from db.connection import get_conn


def track_behavior(user_id: int, action: str, metadata: dict):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO user_behaviors (user_id, action, metadata)
        VALUES (%s, %s, %s)
        """,
        (user_id, action, json.dumps(metadata))
    )

    conn.commit()
    cur.close()
    conn.close()


def get_behaviors(user_id: int):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT action, metadata
        FROM user_behaviors
        WHERE user_id = %s
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "action": row[0],
            "metadata": row[1]
        }
        for row in rows
    ]