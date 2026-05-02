# import sounddevice as sd
# import numpy as np
# import websocket
# import soundfile as sf
# import io
# import time
#
# RATE = 16000
# DURATION = 5
#
# print("🎤 Recording...")
#
# audio = sd.rec(
#     int(DURATION * RATE),
#     samplerate=RATE,
#     channels=1,
#     dtype="int16"
# )
#
# sd.wait()
#
# audio = np.squeeze(audio)
#
# buffer = io.BytesIO()
# sf.write(buffer, audio, RATE, format="WAV", subtype="PCM_16")
#
# wav_bytes = buffer.getvalue()
#
# print("[DEBUG] WAV SIZE:", len(wav_bytes))
#
# ws = websocket.create_connection("ws://127.0.0.1:8000/ws")
#
# # ===== SEND =====
# ws.send(wav_bytes)
#
# # ===== RECEIVE (SAFE) =====
# try:
#     msg = ws.recv()
#     print("SERVER:", msg)
# except Exception as e:
#     print("ERROR:", e)
#
# time.sleep(0.5)
# ws.close()