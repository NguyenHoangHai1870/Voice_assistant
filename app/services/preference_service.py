from app.services.memory_service import save_user_profile


def detect_preferences(user_id: str, text: str):
    text = text.lower()

    if any(x in text for x in [
        "trả lời ngắn gọn thôi",
        "nói ngắn thôi",
        "ngắn gọn thôi",
        "đừng dài dòng"
    ]):
        save_user_profile(user_id, "prefers_short_answer", True)
        return "Đã ghi nhớ bạn thích câu trả lời ngắn gọn."

    if "giải thích kỹ hơn" in text:
        save_user_profile(user_id, "prefers_detailed_answer", True)
        return "Đã ghi nhớ bạn thích giải thích chi tiết."

    if "nói lịch sự hơn" in text:
        save_user_profile(user_id, "prefers_formal_tone", True)
        return "Đã ghi nhớ phong cách trả lời lịch sự."

    if "nói tự nhiên thôi" in text:
        save_user_profile(user_id, "prefers_casual_tone", True)
        return "Đã ghi nhớ phong cách trả lời tự nhiên."

    return None