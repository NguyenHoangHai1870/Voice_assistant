from app.services.qa_router import handle_qa
from app.services.calendar_router import handle_calendar_intent
from app.services.device_control_service import handle_device_control
from app.services.personalization_service import handle_personalization


def execute_intent(user_id: int, text: str, intent: str):

    # CALENDAR DOMAIN
    if intent == "calendar":
        return handle_calendar_intent(user_id, text)

    # CONTROL DEVICE
    elif intent == "control_device":

        result = handle_device_control(text)

        if result["action"] == "open_url":
            import webbrowser
            webbrowser.open(result["url"])
            return "Đã mở theo yêu cầu."

        return "Không hiểu yêu cầu điều khiển."

    # PERSONALIZE
    elif intent == "personalize":
        return handle_personalization(user_id, text)

    # QA
    elif intent == "qa":
        return handle_qa(user_id, text)

    return "Không hiểu yêu cầu."