# from vosk import Model, KaldiRecognizer
# import json
#
# model = Model("model")  # tải model vosk trước
#
# rec = KaldiRecognizer(model, 16000)
#
# def process_audio_chunk(chunk: bytes):
#     if rec.AcceptWaveform(chunk):
#         result = json.loads(rec.Result())
#         return result.get("text", "")
#     else:
#         partial = json.loads(rec.PartialResult())
#         return partial.get("partial", "")
#
# def create_recognizer():
#     return KaldiRecognizer(model, 16000)