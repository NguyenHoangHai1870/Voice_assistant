from pathlib import Path
import joblib
import numpy as np

from app.services.smalltalk_service import (
    is_smalltalk,
    is_weather_query
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "intent_model.pkl"

intent_model = joblib.load(MODEL_PATH)

CONFIDENCE_THRESHOLD = 0.60

def predict_intent(text: str):
    text = text.lower().strip()

    if is_smalltalk(text) or is_weather_query(text):
        return "qa"

    probs = intent_model.predict_proba([[text]])[0]

    best_idx = np.argmax(probs)

    confidence = float(probs[best_idx])

    intent = intent_model.classes_[best_idx]

    print(f"[INTENT] {intent} ({confidence:.2f})")

    if confidence < CONFIDENCE_THRESHOLD:
        return "qa"

    return intent