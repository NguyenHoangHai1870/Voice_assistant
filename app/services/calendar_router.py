import re
from datetime import timedelta

from app.services.calendar_service import (
    add_reminder,
    delete_reminder,
    delete_latest_reminder,
    get_reminders_by_date,
    get_upcoming_reminders
)
from app.services.parser_service import parse_datetime
from app.services.datetime_service import get_now


def handle_calendar_intent(user_id: int, text: str):
    text_lower = text.lower()

    # DELETE CALENDAR
    if any(x in text_lower for x in ["hủy", "xóa", "bỏ lịch"]):

        if len(text.split()) < 4:
            deleted = delete_latest_reminder(user_id)
        else:
            deleted = delete_reminder(user_id, text)

        return (
            "Đã hủy lịch thành công."
            if deleted
            else "Không tìm thấy lịch để hủy."
        )

    # ADD CALENDAR
    if any(x in text_lower for x in ["nhắc", "đặt lịch", "tạo lịch", "lên lịch"]):
        try:
            reminder_time = parse_datetime(text)
        except Exception:
            return "Tôi chưa hiểu thời gian bạn muốn đặt lịch."

        add_reminder(
            user_id=user_id,
            title=text,
            reminder_time=reminder_time
        )

        return "Đã thêm lịch thành công."

    # CHECK CALENDAR
    now = get_now()

    def build_response(title, reminders):
        if not reminders:
            return f"{title} bạn không có lịch nào."

        msg = f"{title} bạn có:\n"
        for reminder_title, reminder_time in reminders:
            msg += f"- {reminder_title} lúc {reminder_time.strftime('%H:%M')}\n"

        return msg

    # hôm nay
    if "hôm nay" in text_lower:
        reminders = get_reminders_by_date(user_id, now.date())
        return build_response("Hôm nay", reminders)

    # ngày mai
    if "mai" in text_lower:
        reminders = get_reminders_by_date(
            user_id,
            now.date() + timedelta(days=1)
        )
        return build_response("Ngày mai", reminders)

    # X ngày nữa
    m = re.search(r"(\d+)\s+ngày\s+nữa", text_lower)
    if m:
        days = int(m.group(1))
        reminders = get_reminders_by_date(
            user_id,
            now.date() + timedelta(days=days)
        )
        return build_response(f"{days} ngày nữa", reminders)

    # tuần này
    if "tuần" in text_lower:
        reminders = get_upcoming_reminders(user_id, 7)

        if not reminders:
            return "Tuần này bạn không có lịch nào."

        msg = "Tuần này bạn có:\n"
        for title, time in reminders:
            msg += f"- {title} lúc {time.strftime('%d/%m %H:%M')}\n"

        return msg

    # mặc định
    reminders = get_upcoming_reminders(user_id, 3)

    if not reminders:
        return "Bạn không có lịch sắp tới."

    msg = "Lịch sắp tới:\n"
    for title, time in reminders:
        msg += f"- {title} lúc {time.strftime('%d/%m %H:%M')}\n"

    return msg