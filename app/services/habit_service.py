from collections import Counter
from app.services.behavior_tracking_service import get_behaviors


def detect_habits(user_id: str):
    behaviors = get_behaviors(user_id)

    alarm_times = []

    for b in behaviors:
        if b["action"] == "add_calendar":
            time = b["metadata"].get("time")
            if time:
                alarm_times.append(time)

    counts = Counter(alarm_times)

    habits = {}

    for time, count in counts.items():
        if count >= 5:
            habits["morning_alarm"] = time

    return habits