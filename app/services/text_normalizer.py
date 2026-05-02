import re


def normalize_text(text: str) -> str:
    text = text.lower().strip()

    # REMOVE / NORMALIZE PUNCTUATION
    text = re.sub(r"[“”\"'`]", "", text)
    text = re.sub(r"[?!.,;:]+", " ", text)
    text = re.sub(r"[-_/]+", " ", text)

    # COMMON STT REPLACEMENTS
    replacements = {
        # question
        "lazi": "là gì",
        "lazy": "là gì",
        "la gi": "là gì",

        # calendar
        "hỷ lịch": "hủy lịch",
        "hỉ lịch": "hủy lịch",
        "huy lich": "hủy lịch",

        # time
        "mấy dờ": "mấy giờ",
        "may gio": "mấy giờ",
        "hom nay": "hôm nay",
        "ngay mai": "ngày mai",

        # apps / brands
        "du túp": "youtube",
        "giu tu be": "youtube",
        "face book": "facebook",
        "gu gồ": "google",
        "cờ rôm": "chrome",

        # tech
        "block chain": "blockchain",
        "git hub": "github",
        "post gre": "postgres",
    }

    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)

    # REMOVE FILLER / NOISE WORDS
    filler_patterns = [
        r"\bờ+\b",
        r"\bà+\b",
        r"\bơ+\b",
        r"\bum+\b",
        r"\buh+\b",
        r"\bờm+\b",
    ]

    for pattern in filler_patterns:
        text = re.sub(pattern, " ", text)

    # FIX DUPLICATE SPACES
    text = re.sub(r"\s+", " ", text).strip()

    return text