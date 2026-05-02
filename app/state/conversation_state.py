LAST_EXPECTED_FIELD = {}


def set_expected_field(user_id: str, field: str):
    LAST_EXPECTED_FIELD[user_id] = field


def get_expected_field(user_id: str):
    return LAST_EXPECTED_FIELD.get(user_id)


def clear_expected_field(user_id: str):
    LAST_EXPECTED_FIELD.pop(user_id, None)