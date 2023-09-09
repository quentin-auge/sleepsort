from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
import time
from typing import Iterable
from urllib.parse import parse_qs


def app(environ, start_response):
    headers = [
        ("Content-type", "text/plain"),
    ]

    wait_arg = parse_qs(environ["QUERY_STRING"]).get("wait")
    if not wait_arg:
        start_response("500", headers)
        return [b"Expected a ?wait= arg\n"]

    start_response("200", headers)

    seconds = int(wait_arg[0])
    time.sleep(seconds)

    return []