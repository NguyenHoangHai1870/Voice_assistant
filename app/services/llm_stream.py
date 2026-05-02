# import requests
# import json
#
# OLLAMA_URL = "http://localhost:11434/api/chat"
# MODEL = "qwen2.5:1.5b"
#
# def stream_llm(messages):
#
#     payload = {
#         "model": MODEL,
#         "messages": messages,
#         "stream": True
#     }
#
#     with requests.post(OLLAMA_URL, json=payload, stream=True) as r:
#         for line in r.iter_lines():
#             if line:
#                 data = json.loads(line.decode("utf-8"))
#
#                 if "message" in data:
#                     yield data["message"]["content"]