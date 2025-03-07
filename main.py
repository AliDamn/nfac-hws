from wsgiref.simple_server import make_server
from fastapi import FastAPI

# 1. server-ping-pong
def ping_pong_app(environ, start_response):
    if environ["REQUEST_METHOD"] == "GET" and environ["PATH_INFO"] == "/ping":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [b"pong"]
    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Not Found"]

# 2. server-request-info
def request_info_app(environ, start_response):
    if environ["REQUEST_METHOD"] == "GET" and environ["PATH_INFO"] == "/info":
        info = "\n".join([
            environ["REQUEST_METHOD"],
            environ["RAW_URI"],
            environ["SERVER_PROTOCOL"]
        ])
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [info.encode()]
    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Not Found"]

# 3. fastapi-hello
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, nfactorial!"}

# 4. fastapi-meaning-life
@app.post("/meaning-of-life")
def meaning_of_life():
    return {"meaning": "42"}

if __name__ == "__main__":
    server = make_server("", 8000, ping_pong_app)
    server.serve_forever()

