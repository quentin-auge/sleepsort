import asyncio
import random
from urllib.parse import parse_qs

import websockets

host = "127.0.0.1"
ws = None
initialized = False

async def app(scope, receive, send):
    global ws, initialized

    await send({
        "type": "websocket.accept"
    })

    if not initialized:
        initialized = True
        ws = await websockets.connect(f"ws://{host}:8000/")
        await ws.send("1")

    try:
        while True:
            request = await receive()

            if request["type"] == "websocket.disconnect":
                print("Bye!")
                break

            if request["type"] == "websocket.receive":
                print("sleep " + request["text"])
                n_seconds = int(request["text"].split(" ")[-1])
                n = int(n_seconds)
                await asyncio.sleep(n)
                await ws.send(f"{random.randint(1, 10)}")

    except Exception as e:
        print("Error")
        await send({"type": "websocket.close", "code": 1011, "reason": "Server Error"})
        raise e

    finally:
        await ws.close()