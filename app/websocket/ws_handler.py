# from fastapi import WebSocket
# from app.services.stt_stream import process_audio_chunk
#
# async def handle_ws(websocket: WebSocket):
#     await websocket.accept()
#
#     try:
#         while True:
#             audio_chunk = await websocket.receive_bytes()
#
#             text = process_audio_chunk(audio_chunk)
#
#             if text:
#                 await websocket.send_json({
#                     "type": "stt",
#                     "data": text
#                 })
#
#     except Exception as e:
#         print("WS ERROR:", e)