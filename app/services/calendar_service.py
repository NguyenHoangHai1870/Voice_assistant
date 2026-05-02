from datetime import timedelta
from app.services.parser_service import parse_datetime
from db.connection import get_conn
from app.services.datetime_service import get_now

def add_reminder(user_id: int, title: str, reminder_time):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO reminders (user_id, title, reminder_time)
        VALUES (%s, %s, %s)
    """, (user_id, title, reminder_time))

    conn.commit()
    cur.close()
    conn.close()

def get_reminders_by_date(user_id: int, target_date):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT title, reminder_time
        FROM reminders
        WHERE user_id = %s
        AND DATE(reminder_time) = %s
        ORDER BY reminder_time
    """, (user_id, target_date))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def get_upcoming_reminders(user_id: int, days=7):
    conn = get_conn()
    cur = conn.cursor()

    now = get_now()
    future = now + timedelta(days=days)

    cur.execute("""
        SELECT title, reminder_time
        FROM reminders
        WHERE user_id = %s
        AND reminder_time BETWEEN %s AND %s
        ORDER BY reminder_time
    """, (user_id, now, future))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows




def delete_reminder(user_id: int, text: str):
    conn = get_conn()
    cur = conn.cursor()

    try:
        target_time = parse_datetime(text)

        print("PARSED TIME:", target_time)

        # 👉 match theo NGÀY + GIỜ (ổn định nhất)
        cur.execute("""
            DELETE FROM reminders
            WHERE user_id = %s
            AND DATE(reminder_time) = %s
            AND EXTRACT(HOUR FROM reminder_time) = %s
            RETURNING id
        """, (
            user_id,
            target_time.date(),
            target_time.hour
        ))

        result = cur.fetchone()
        conn.commit()

        return result is not None

    except Exception as e:
        print("DELETE ERROR:", e)
        return False

    finally:
        cur.close()
        conn.close()

def delete_latest_reminder(user_id: int):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM reminders
        WHERE id = (
            SELECT id FROM reminders
            WHERE user_id = %s
            ORDER BY reminder_time ASC
            LIMIT 1
        )
        RETURNING id
    """, (user_id,))

    result = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    return result is not None