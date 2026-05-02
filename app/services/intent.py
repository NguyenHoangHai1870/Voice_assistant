from pathlib import Path
import joblib
from app.services.smalltalk_service import is_smalltalk, is_weather_query
BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_PATH = BASE_DIR / "models" / "intent_model.pkl"

intent_model = joblib.load(MODEL_PATH)

def predict_intent(text: str):
    text_lower = text.lower().strip()

    if is_smalltalk(text_lower) or is_weather_query(text_lower):
        return "qa"

    return intent_model.predict([text])[0]