import re
from app.services.weather_service import get_weather


TIME_PATTERNS = [
    "mấy giờ",
    "bây giờ là mấy giờ",
    "hiện tại mấy giờ",
    "giờ hiện tại",
    "hôm nay ngày mấy",
    "hôm nay là ngày bao nhiêu",
    "ngày tháng năm hiện tại",
    "thời gian hiện tại"
]


SMALLTALK_PATTERNS = [
    r"\b(chào|hello|hi|hey|xin chào)\b",
    r"\b(chào bạn)\b",
    r"\b(chào nhé)\b",
    r"\b(chào nha)\b",
    r"\bbạn tên gì\b",
    r"\btên bạn là gì\b",
    r"\bbạn là ai\b",
    r"\bai tạo ra bạn\b",
    r"\bhow are you\b",
    r"\bbạn khỏe không\b"
]


WEATHER_PATTERNS = [
    r"\bthời tiết\b",
    r"\bweather\b",
    r"\bhôm nay nóng không\b",
    r"\bhôm nay lạnh không\b",
    r"\bcó mưa không\b",
    r"\bnhiệt độ hôm nay\b",
    r"\btrời hôm nay thế nào\b",
    r"\bngoài trời thế nào\b"
]


def is_smalltalk(text: str) -> bool:
    text = text.lower().strip()

    return any(re.search(p, text) for p in SMALLTALK_PATTERNS)


def is_weather_query(text: str) -> bool:
    text = text.lower().strip()

    return any(re.search(p, text) for p in WEATHER_PATTERNS)


def handle_smalltalk(text: str) -> str | None:
    text = text.lower().strip()

    # WEATHER
    if is_weather_query(text):
        return get_weather()

    # NAME / IDENTITY
    if re.search(r"\b(bạn tên gì|tên bạn là gì)\b", text):
        return "Tôi là Hari, trợ lý AI của bạn."

    if re.search(r"\b(bạn là ai|ai tạo ra bạn)\b", text):
        return "Tôi là Hari, trợ lý AI được tạo để hỗ trợ bạn."

    # GREETING
    if re.search(r"\b(chào|hello|hi|hey|xin chào)\b", text):
        return "Chào bạn, tôi có thể giúp gì?"

    # STATUS
    if re.search(r"\b(bạn khỏe không|how are you)\b", text):
        return "Tôi hoạt động tốt. Còn bạn thì sao?"

    return None