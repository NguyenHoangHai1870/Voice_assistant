import re

from app.config.memory_patterns import MEMORY_RULES
from app.services.memory_service import (
    save_user_profile,
    save_multi_value_profile,
    get_user_profile
)
from app.services.preference_service import detect_preferences
from app.state.conversation_state import (
    set_expected_field,
    get_expected_field,
    clear_expected_field
)


STRONG_MEMORY_CUES = [
    "tôi là",
    "tôi tên",
    "tôi thích",
    "tôi quê",
    "tôi học",
    "tôi làm",
    "mình là",
    "mình thích",
    "mình học",
]


def is_confident_memory_statement(text: str) -> bool:
    return any(cue in text for cue in STRONG_MEMORY_CUES)


def is_invalid_memory_value(value: str) -> bool:
    invalid_keywords = [
        "gì",
        "bao nhiêu",
        "ở đâu",
        "khi nào",
        "là ai",
        "thế nào"
    ]

    return any(k in value for k in invalid_keywords)


def save_memory_with_update_check(user_id, field, value):
    profile = get_user_profile(user_id)
    old_value = profile.get(field)

    if field == "hobbies":
        save_multi_value_profile(user_id, field, value)

        if old_value and value not in old_value:
            return f"Đã thêm sở thích mới: {value}."

        return f"Đã ghi nhớ sở thích của bạn là {value}."

    if old_value and old_value != value:
        save_user_profile(user_id, field, value)
        return f"Đã cập nhật {field} từ {old_value} thành {value}."

    save_user_profile(user_id, field, value)
    return None


def handle_context_followup(user_id: str, text: str):
    expected_field = get_expected_field(user_id)

    if not expected_field:
        return None

    clear_expected_field(user_id)

    save_user_profile(user_id, expected_field, text)

    return f"Đã ghi nhớ {expected_field} của bạn là {text}."


def handle_personalization(user_id: str, text: str):
    text = text.lower().strip()

    pref_response = detect_preferences(user_id, text)
    if pref_response:
        return pref_response

    followup_response = handle_context_followup(user_id, text)
    if followup_response:
        return followup_response

    if not is_confident_memory_statement(text):
        return None

    for rule in MEMORY_RULES:
        for pattern in rule["patterns"]:
            m = re.search(pattern, text)

            if not m:
                continue

            value = m.group(1).strip()

            if is_invalid_memory_value(value):
                return None

            update_msg = save_memory_with_update_check(
                user_id,
                rule["field"],
                value
            )

            if update_msg:
                return update_msg

            if rule["field"] == "education":
                set_expected_field(user_id, "major")
                return (
                    rule["template"].format(value)
                    + " Bạn học ngành gì?"
                )

            return rule["template"].format(value)

    return None