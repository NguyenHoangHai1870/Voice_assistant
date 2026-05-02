# app/services/query_classifier.py

def classify_query(text: str) -> str:
    text = text.lower().strip()

    # small talk / chit-chat
    small_talk = [
        "bạn tên gì",
        "mấy giờ rồi",
        "chào",
        "hello",
        "hi",
        "kể chuyện",
        "bạn là ai",
        "bạn bao nhiêu tuổi"
    ]

    for s in small_talk:
        if s in text:
            return "small_talk"

    # câu quá ngắn
    if len(text.split()) <= 2:
        return "unclear"

    return "knowledge"