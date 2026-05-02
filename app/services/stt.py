import time
from faster_whisper import WhisperModel

model = WhisperModel(
    "medium",
    device="cpu",
    compute_type="int8"
)

DOMAIN_PROMPT = "Hội thoại tiếng Việt về AI và công nghệ."
def speech_to_text(audio_path: str) -> str:
    try:
        print("[STT FILE]:", audio_path)

        segments, info = model.transcribe(
            audio_path,
            language="vi",
            beam_size=3,
            vad_filter=True
        )

        text = "".join(seg.text for seg in segments).strip()

        print("[STT RAW]:", repr(text))

        if not text:
            print("⚠️ STT EMPTY")
            return ""

        return text.lower()

    except Exception as e:
        print("🔥 STT ERROR:", repr(e))
        return ""