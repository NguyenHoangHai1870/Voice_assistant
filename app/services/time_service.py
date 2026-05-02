import re
from datetime import timedelta, datetime
from app.services.datetime_service import get_now

WEEKDAYS = [
    "Thứ Hai", "Thứ Ba", "Thứ Tư",
    "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"
]


def handle_time_query(text: str):
    text = text.lower().strip()
    now = get_now()

    # ===== CURRENT TIME =====
    if "mấy giờ" in text or "giờ hiện tại" in text:
        return f"Bây giờ là {now.strftime('%H:%M:%S')}."

    # ===== TODAY =====
    if "hôm nay" in text:
        if "ngày" in text:
            return f"Hôm nay là ngày {now.strftime('%d/%m/%Y')}."
        if "thứ" in text:
            return f"Hôm nay là {WEEKDAYS[now.weekday()]}."

    # ===== TOMORROW =====
    if "ngày mai" in text:
        tmr = now + timedelta(days=1)
        return f"Ngày mai là {tmr.strftime('%d/%m/%Y')} ({WEEKDAYS[tmr.weekday()]})."

    # ===== YESTERDAY =====
    if "hôm qua" in text:
        ytd = now - timedelta(days=1)
        return f"Hôm qua là {ytd.strftime('%d/%m/%Y')} ({WEEKDAYS[ytd.weekday()]})."

    # ===== X DAYS LATER =====
    m = re.search(r"(\d+)\s+ngày\s+nữa", text)
    if m:
        days = int(m.group(1))
        future = now + timedelta(days=days)
        return f"{days} ngày nữa là {future.strftime('%d/%m/%Y')} ({WEEKDAYS[future.weekday()]})."

    # ===== X DAYS AGO =====
    m = re.search(r"(\d+)\s+ngày\s+trước", text)
    if m:
        days = int(m.group(1))
        past = now - timedelta(days=days)
        return f"{days} ngày trước là {past.strftime('%d/%m/%Y')} ({WEEKDAYS[past.weekday()]})."

    # ===== X WEEKS LATER =====
    m = re.search(r"(\d+)\s+tuần\s+nữa", text)
    if m:
        weeks = int(m.group(1))
        future = now + timedelta(weeks=weeks)
        return f"{weeks} tuần nữa là {future.strftime('%d/%m/%Y')} ({WEEKDAYS[future.weekday()]})."

    # ===== DAY OF WEEK =====
    if "thứ mấy" in text:
        return f"Hôm nay là {WEEKDAYS[now.weekday()]}."

    # ===== FULL DATE =====
    if "ngày tháng năm hiện tại" in text or "thời gian hiện tại" in text:
        return now.strftime("Hiện tại là %H:%M:%S ngày %d/%m/%Y.")

    # ===== COUNTDOWN TẾT =====
    if "tết" in text:
        tet = get_tet_date(now.year)

        if now > tet:
            tet = get_tet_date(now.year + 1)

        diff = (tet - now).days
        return f"Còn {diff} ngày nữa đến Tết."

    return None


def get_tet_date(year: int):
    TET_DATES = {
        2025: (1, 29),
        2026: (2, 17),
        2027: (2, 6)
    }

    if year in TET_DATES:
        month, day = TET_DATES[year]
        return datetime(year, month, day, tzinfo=get_now().tzinfo)

    return datetime(year, 2, 10, tzinfo=get_now().tzinfo)