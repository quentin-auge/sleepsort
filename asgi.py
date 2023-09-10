import asyncio
from urllib.parse import parse_qs

async def app(scope, receive, send):
    headers = [
        ("Content-type", "text/plain"),
    ]

    wait_arg = parse_qs(scope["query_string"]).get(b"wait")

    if not wait_arg:
        await send({
            "type": "http.response.start",
            "status": 500,
            "headers": headers
        })

        await send({
            "type": "http.response.body",
            "body": b"Expected a ?wait= arg\n",
        })

        return

    seconds = int(wait_arg[0])
    await asyncio.sleep(seconds)

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": headers
    })

    await send({
        "type": "http.response.body",
        "body": b"",
    })