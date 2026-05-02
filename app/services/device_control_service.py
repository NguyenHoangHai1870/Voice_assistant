import urllib.parse


WEB_APPS = {
    # SOCIAL
    "facebook": "https://www.facebook.com",
    "fb": "https://www.facebook.com",
    "messenger": "https://www.messenger.com",
    "instagram": "https://www.instagram.com",
    "tiktok": "https://www.tiktok.com",

    # VIDEO
    "youtube": "https://www.youtube.com",
    "netflix": "https://www.netflix.com",
    "twitch": "https://www.twitch.tv",

    # GOOGLE
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",

    # AI TOOLS
    "chatgpt": "https://chat.openai.com",
    "gpt": "https://chat.openai.com",
    "gemini": "https://gemini.google.com",

    # WORK
    "drive": "https://drive.google.com",
    "docs": "https://docs.google.com",
    "sheet": "https://docs.google.com/spreadsheets",
    "calendar": "https://calendar.google.com",

    # DEV
    "github": "https://github.com",
    "stackoverflow": "https://stackoverflow.com",
}


REMOVE_WORDS = [
    "mở", "open", "truy cập", "vào", "xem", "search",
    "tìm", "website", "trên", "giúp tôi mở"
]


def clean_query(text: str):
    q = text.lower()
    for w in REMOVE_WORDS:
        q = q.replace(w, "")
    return q.strip()


def extract_search(text: str):
    """Lấy keyword tìm kiếm nếu có"""
    return clean_query(text)


def handle_device_control(text: str):
    text_lower = text.lower()

    # 1. WEB APPS (OPEN DIRECT)
    for key, url in WEB_APPS.items():
        if key in text_lower:

            # nếu có search query (youtube, google, etc.)
            if key in ["youtube", "google", "gmail"]:
                query = extract_search(text_lower)

                if query and key in ["youtube", "google"]:
                    search_url = {
                        "youtube": "https://www.youtube.com/results?search_query=",
                        "google": "https://www.google.com/search?q="
                    }

                    url = search_url[key] + urllib.parse.quote(query)

            return {
                "action": "open_url",
                "url": url
            }

    # 2. SEARCH FALLBACK
    if any(x in text_lower for x in ["tìm", "search"]):
        query = extract_search(text_lower)

        if query:
            return {
                "action": "open_url",
                "url": "https://www.google.com/search?q=" + urllib.parse.quote(query)
            }

    return {"action": "unknown"}