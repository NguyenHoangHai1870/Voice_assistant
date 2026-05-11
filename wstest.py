import asyncio
import websockets


async def test():
    uri = "ws://127.0.0.1:8000/ws"

    async with websockets.connect(uri) as websocket:
        print("Connected")

        with open("kcc.m4a", "rb") as f:
            audio = f.read()

        await websocket.send(audio)

        response = await websocket.recv()
        print("Response:", response)


asyncio.run(test())