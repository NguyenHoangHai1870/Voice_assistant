from collections import defaultdict, deque

from db.user_profile_repo import save_user_profile as db_save_user_profile
from db.user_profile_repo import get_user_profile as db_get_user_profile


# SHORT TERM CONTEXT MEMORY
CONTEXT_MEMORY = defaultdict(lambda: deque(maxlen=5))


def save_context(user_id: str, role: str, text: str):
    CONTEXT_MEMORY[user_id].append({
        "role": role,
        "text": text
    })


def get_context(user_id: str):
    return list(CONTEXT_MEMORY[user_id])


# PROFILE MEMORY
def save_user_profile(user_id: str, field: str, value: str):
    db_save_user_profile(user_id, field, value)


def get_user_profile(user_id: str):
    profile = db_get_user_profile(user_id)
    return profile or {}


# MULTI VALUE PROFILE
def save_multi_value_profile(user_id: str, field: str, value: str):
    profile = get_user_profile(user_id)

    current = profile.get(field)

    if not current:
        save_user_profile(user_id, field, value)
        return

    values = [v.strip() for v in current.split(",") if v.strip()]

    if value not in values:
        values.append(value)

    save_user_profile(user_id, field, ", ".join(values))