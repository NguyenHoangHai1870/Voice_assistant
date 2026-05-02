import re
from datetime import timedelta
from app.services.datetime_service import get_now


def parse_relative_datetime(text: str):
    now = get_now()

    m = re.search(r"(\d+)\s+ngày\s+nữa", text)
    if m:
        return now + timedelta(days=int(m.group(1)))

    m = re.search(r"(\d+)\s+ngày\s+trước", text)
    if m:
        return now - timedelta(days=int(m.group(1)))

    m = re.search(r"(\d+)\s+tuần\s+nữa", text)
    if m:
        return now + timedelta(weeks=int(m.group(1)))

    return None