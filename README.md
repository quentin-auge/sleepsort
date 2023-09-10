# Sleepsort

## WSGI

### Server

`gunicorn --reload --workers 2 wsgi:app`

### Client

`curl http://127.0.0.1:8000/?wait=3`

## ASGI

### Server

`uvicorn --reload asgi:app`

### Client

`curl http://127.0.0.1:8000/`