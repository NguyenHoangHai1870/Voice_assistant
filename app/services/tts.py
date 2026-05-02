# import pyttsx3
# import asyncio
#
# engine = pyttsx3.init()
#
# def speak(text: str):
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print("TTS ERROR:", e)
#
#
# async def speak_chunk(text: str):
#     await asyncio.to_thread(speak, text)