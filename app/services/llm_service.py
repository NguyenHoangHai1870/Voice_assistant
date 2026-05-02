import requests
from app.config.settings import OLLAMA_MODEL
from app.services.memory_service import get_context, get_user_profile

OLLAMA_URL = "http://localhost:11434/api/chat"


def clean_llm_output(answer: str) -> str:
    answer = answer.strip()

    prefixes = ["Assistant:", "Trợ lý:", "AI:"]

    for p in prefixes:
        if answer.startswith(p):
            answer = answer[len(p):].strip()

    answer = "\n".join(
        line.strip()
        for line in answer.splitlines()
        if line.strip()
    )

    return answer


def build_style_prompt(profile: dict) -> str:
    rules = []

    if profile.get("prefers_short_answer"):
        rules.extend([
            "Trả lời tối đa 3 câu hoặc 5 bullet.",
            "Không lan man.",
            "Chỉ nêu ý chính."
        ])

    if profile.get("prefers_detailed_answer"):
        rules.extend([
            "Trả lời chi tiết.",
            "Giải thích từng bước rõ ràng."
        ])

    if profile.get("prefers_formal_tone"):
        rules.append("Dùng giọng điệu lịch sự, trang trọng.")

    if profile.get("prefers_casual_tone"):
        rules.append("Dùng giọng điệu tự nhiên, thân thiện.")

    return "\n".join(f"- {r}" for r in rules)


def generate_llm_answer(user_id: str, text: str) -> str:
    try:
        # ===== GUARD (TRÁNH GỌI LLM VÔ NGHĨA) =====
        if len(text.split()) <= 2:
            return "Bạn có thể nói rõ hơn không?"

        # ===== CONTEXT (RÚT GỌN + FORMAT LẠI) =====
        raw_context = get_context(user_id)[-2:]

        context_str = "\n".join(
            f"{c['role']}: {c['text']}"
            for c in raw_context
        )

        # ===== PROFILE (FILTER + FORMAT) =====
        full_profile = get_user_profile(user_id)

        profile = {
            k: v for k, v in full_profile.items()
            if v and k in [
                "name",
                "hobbies",
                "favorite_food",
                "prefers_short_answer",
                "prefers_detailed_answer"
            ]
        }

        profile_str = "\n".join(
            f"{k}: {v}" for k, v in profile.items()
        ) if profile else "Không có"

        # ===== STYLE PROMPT =====
        style_prompt = build_style_prompt(full_profile)

        # ===== MESSAGES =====
        messages = [
            {
                "role": "system",
                "content": f"""
Bạn là trợ lý AI tiếng Việt.

LUẬT:
- Chỉ trả lời bằng tiếng Việt
- Không dùng tiếng Trung, Nhật, Hàn

Phong cách:
{style_prompt}
"""
            },
            {
                "role": "user",
                "content": f"""
Thông tin người dùng:
{profile_str}

Lịch sử hội thoại:
{context_str}

Câu hỏi:
{text}
"""
            }
        ]

        # ===== CALL LLM =====
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 150
                }
            },
            timeout=30
        )

        data = res.json()

        if "message" in data and "content" in data["message"]:
            return clean_llm_output(data["message"]["content"])

        if "response" in data:
            return clean_llm_output(data["response"])

        if "error" in data:
            return f"Lỗi LLM: {data['error']}"

        return "Tôi không thể trả lời lúc này."

    except Exception as e:
        return f"Lỗi gọi LLM: {str(e)}"