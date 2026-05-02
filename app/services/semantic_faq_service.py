import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer


# ===== PATH CONFIG =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

EMBED_PATH = os.path.join(BASE_DIR, "models", "faq_embeddings.npy")
MAP_PATH = os.path.join(BASE_DIR, "models", "faq_index_map.json")


# ===== LOAD MODEL =====
model = SentenceTransformer("intfloat/multilingual-e5-small")


# ===== LOAD DATA =====
FAQ_EMBEDDINGS = np.load(EMBED_PATH)

with open(MAP_PATH, "r", encoding="utf-8") as f:
    FAQ_INDEX_MAP = json.load(f)


# ===== MAIN FUNCTION =====
def retrieve_faq(query: str):
    query_embedding = model.encode(
        [f"query: {query}"],
        normalize_embeddings=True
    )[0].astype(np.float32)

    scores = np.dot(FAQ_EMBEDDINGS, query_embedding)
    ranked_indices = np.argsort(scores)[::-1]

    best_idx = ranked_indices[0]
    second_idx = ranked_indices[1]

    best_score = float(scores[best_idx])
    second_score = float(scores[second_idx])

    margin = best_score - second_score

    faq_item = FAQ_INDEX_MAP[best_idx]

    FAQ_BLOCK_KEYWORDS = [
        "hướng dẫn",
        "cách",
        "làm sao",
        "như thế nào",
        "tại sao",
        "gợi ý",
        "nên",
        "help"
    ]

    if any(k in query.lower() for k in FAQ_BLOCK_KEYWORDS):
        return {
            "faq": None,
            "score": 0,
            "margin": 0,
            "is_valid": False
        }

    is_valid = (
            best_score >= 0.88 and
            margin >= 0.03
    )

    return {
        "faq": faq_item,
        "score": best_score,
        "margin": margin,
        "is_valid": is_valid
    }