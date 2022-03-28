from uvicorn import run
from fastapi import FastAPI


app = FastAPI(
    title="Simple Auth",
)


@app.get("/")
def index():
    return {"message": "Hello World"}


if __name__ == "__main__":
    run(app, 
        host="127.0.0.1",
        port=8432,
        ssl_keyfile= "key.pem",
        ssl_certfile= "cert.pem",
        debug=True)
