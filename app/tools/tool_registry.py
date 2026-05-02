from app.services.calendar_service import add_reminder
from datetime import timedelta
from app.services.datetime_service import get_now

tomorrow = get_now().date() + timedelta(days=1)
TOOLS = {
    "add_calendar": add_reminder,
    "check_calendar": tomorrow
}