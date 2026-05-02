from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uuid
import os
import asyncio
from app.orchestrator import Orchestrator

app = FastAPI()
orchestrator = Orchestrator()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        filename = None

        try:
            data = await websocket.receive_bytes()

            filename = f"temp_{uuid.uuid4()}.m4a"

            with open(filename, "wb") as f:
                f.write(data)

            response = await asyncio.to_thread(
                orchestrator.process_audio,
                user_id=1,
                audio_path=filename
            )

            await websocket.send_json(response)

        except WebSocketDisconnect:
            break

        except Exception as e:
            print("WS ERROR:", repr(e))
            break

        finally:
            if filename and os.path.exists(filename):
                os.remove(filename)