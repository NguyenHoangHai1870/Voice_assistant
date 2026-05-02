from app.services.habit_service import detect_habits
from app.services.calendar_service import add_reminder, get_reminders_by_date
from app.services.datetime_service import get_now
from datetime import timedelta


def check_proactive_suggestions(user_id: str):
    habits = detect_habits(user_id)

    tomorrow = get_now().date() + timedelta(days=1)
    reminders = get_reminders_by_date(user_id, tomorrow)

    reminder_times = [r[1].strftime("%H:%M") for r in reminders]

    if "morning_alarm" in habits:
        habit_time = habits["morning_alarm"]

        if habit_time not in reminder_times:
            return (
                f"Bạn thường đặt lịch lúc {habit_time}, "
                "hôm nay chưa thấy tạo. Bạn có muốn tôi thêm không?"
            )

    return None