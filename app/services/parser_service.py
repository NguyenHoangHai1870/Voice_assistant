import re
from datetime import timedelta
from app.services.datetime_service import get_now


def parse_datetime(text: str):
    text = text.lower()
    now = get_now()

    # ===== DEFAULT =====
    target_date = now.date()
    hour = 9
    minute = 0

    # ===== TIME (fix mạnh hơn) =====
    m = re.search(r"(\d{1,2})(?:h| giờ)?(?:\s*(\d{1,2}))?", text)
    if m:
        hour = int(m.group(1))
        minute = int(m.group(2)) if m.group(2) else 0

    # ===== MORNING / AFTERNOON =====
    if "chiều" in text or "tối" in text:
        if hour < 12:
            hour += 12

    # ===== RELATIVE DATE =====
    if "mai" in text:
        target_date = now.date() + timedelta(days=1)

    m = re.search(r"(\d+)\s+ngày\s+nữa", text)
    if m:
        target_date = now.date() + timedelta(days=int(m.group(1)))

    # ===== ABSOLUTE DATE (4 tháng 5) =====
    m = re.search(r"ngày\s*(\d{1,2})\s*tháng\s*(\d{1,2})", text)
    if m:
        day = int(m.group(1))
        month = int(m.group(2))
        target_date = target_date.replace(day=day, month=month)

    # ===== dd/mm =====
    m = re.search(r"(\d{1,2})/(\d{1,2})", text)
    if m:
        day = int(m.group(1))
        month = int(m.group(2))
        target_date = target_date.replace(day=day, month=month)

    return now.replace(
        year=target_date.year,
        month=target_date.month,
        day=target_date.day,
        hour=hour,
        minute=minute,
        second=0,
        microsecond=0
    )