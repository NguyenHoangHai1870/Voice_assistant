from db.behavior_repo import track_behavior as repo_track_behavior
from db.behavior_repo import get_behaviors as repo_get_behaviors


def track_behavior(user_id: int, action: str, metadata: dict):
    repo_track_behavior(user_id, action, metadata)


def get_behaviors(user_id: int):
    return repo_get_behaviors(user_id)