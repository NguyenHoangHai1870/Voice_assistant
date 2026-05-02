from db.connection import get_conn


def save_context(user_id: int, role: str, text: str):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO conversation_memory (user_id, role, content)
        VALUES (%s, %s, %s)
        """,
        (user_id, role, text)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_context(user_id: int, limit: int = 5):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT role, content
        FROM conversation_memory
        WHERE user_id = %s
        ORDER BY created_at DESC
        LIMIT %s
        """,
        (user_id, limit)
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {"role": r[0], "text": r[1]}
        for r in reversed(rows)
    ]