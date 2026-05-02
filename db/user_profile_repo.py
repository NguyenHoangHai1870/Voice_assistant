from db.connection import get_conn


def save_user_profile(user_id: int, key: str, value):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        f"""
        INSERT INTO user_profiles (user_id, {key})
        VALUES (%s, %s)
        ON CONFLICT (user_id)
        DO UPDATE SET
            {key} = EXCLUDED.{key},
            updated_at = CURRENT_TIMESTAMP
        """,
        (user_id, value)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_user_profile(user_id: int):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM user_profiles WHERE user_id = %s",
        (user_id,)
    )

    row = cur.fetchone()

    if not row:
        cur.close()
        conn.close()
        return {}

    columns = [desc[0] for desc in cur.description]

    profile = dict(zip(columns, row))

    cur.close()
    conn.close()

    return profile