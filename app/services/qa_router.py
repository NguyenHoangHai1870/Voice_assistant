from app.services.semantic_faq_service import retrieve_faq
from app.services.llm_service import generate_llm_answer
from app.services.personalization_service import handle_personalization
from app.services.memory_service import get_user_profile
from app.config.memory_patterns import PROFILE_QUERY_PATTERNS
from app.services.smalltalk_service import is_smalltalk, handle_smalltalk
from app.services.time_service import handle_time_query
from app.config.time_patterns import TIME_PATTERNS
import re


def retrieve_profile_answer(profile: dict, text: str):
    for rule in PROFILE_QUERY_PATTERNS:
        for pattern in rule["patterns"]:
            if re.search(pattern, text):
                value = profile.get(rule["field"])

                if value:
                    return rule["template"].format(value)

                return "Tôi chưa biết thông tin đó về bạn."

    return None


def handle_qa(user_id: str, text: str):
    text = text.lower().strip()

    # ===== TIME =====
    time_answer = handle_time_query(text)
    if time_answer:
        return time_answer

    # ===== WEATHER =====
    if "thời tiết" in text or "weather" in text:
        return handle_smalltalk(text)

    # ===== SMALLTALK =====
    if is_smalltalk(text):
        return handle_smalltalk(text)

    # ===== MEMORY QUERY =====
    profile = get_user_profile(user_id)
    memory_answer = retrieve_profile_answer(profile, text)
    if memory_answer:
        return memory_answer

    # ===== MEMORY UPDATE =====
    personalization_response = handle_personalization(user_id, text)
    if personalization_response:
        return personalization_response

    # ===== FAQ =====
    result = retrieve_faq(text)
    if result["is_valid"]:
        return result["faq"]["answer"]

    # ===== LLM FALLBACK =====
    return generate_llm_answer(user_id, text)