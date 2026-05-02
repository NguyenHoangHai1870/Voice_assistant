import time
from app.services.stt import speech_to_text
from app.services.intent import predict_intent
from app.services.response_service import execute_intent
from app.services.memory_service import save_context
from app.services.proactive_service import check_proactive_suggestions
from app.services.text_normalizer import normalize_text


class Orchestrator:

    # AUDIO FLOW
    def process_audio(self, user_id: int, audio_path: str):

        try:
            t0 = time.time()

            # ===== STT =====
            text = speech_to_text(audio_path).strip()
            text = normalize_text(text)
            print(f"[TIME] STT: {time.time() - t0:.2f}s")

            # ===== PROACTIVE =====
            proactive_msg = check_proactive_suggestions(user_id)
            if proactive_msg:
                return {"type": "text", "data": proactive_msg}

            # ===== SAVE USER =====
            save_context(user_id, "user", text)

            # ===== INTENT =====
            t1 = time.time()
            intent = predict_intent(text)
            print(f"[INTENT]: {intent}")
            print(f"[TIME] INTENT: {time.time() - t1:.2f}s")

            # ===== EXECUTE =====
            t2 = time.time()
            response = execute_intent(user_id, text, intent)

            print(f"[TIME] EXECUTE: {time.time() - t2:.2f}s")
            print(f"[TIME] TOTAL: {time.time() - t0:.2f}s")

            # ===== SAVE ASSISTANT (CHỈ LƯU TEXT) =====
            if isinstance(response, dict) and response.get("type") == "text":
                save_context(user_id, "assistant", response["data"])

            return response

        except Exception as e:
            print("ORCHESTRATOR ERROR:", repr(e))
            return {"type": "text", "data": "Có lỗi xảy ra"}

    # TEXT FLOW
    def process_text(self, user_id: int, text: str):

        try:
            t0 = time.time()

            text = text.strip()
            print(f"[INPUT]: {text}")

            # ===== PROACTIVE =====
            proactive_msg = check_proactive_suggestions(user_id)
            if proactive_msg:
                print("[PROACTIVE]: Triggered")
                return {"type": "text", "data": proactive_msg}

            # ===== SAVE USER =====
            save_context(user_id, "user", text)

            # ===== INTENT =====
            t1 = time.time()
            intent = predict_intent(text)
            print(f"[INTENT]: {intent}")
            print(f"[TIME] INTENT: {time.time() - t1:.2f}s")

            # ===== EXECUTE =====
            t2 = time.time()
            response = execute_intent(user_id, text, intent)

            print(f"[TIME] EXECUTE: {time.time() - t2:.2f}s")
            print(f"[TIME] TOTAL: {time.time() - t0:.2f}s")

            # ===== SAVE ASSISTANT =====
            if isinstance(response, dict) and response.get("type") == "text":
                save_context(user_id, "assistant", response["data"])

            print(f"[RESPONSE]: {response}")

            if isinstance(response, dict):
                return response.get("data", "")

            return response

        except Exception as e:
            print("ORCHESTRATOR TEXT ERROR:", repr(e))
            return {"type": "text", "data": "Có lỗi xảy ra"}