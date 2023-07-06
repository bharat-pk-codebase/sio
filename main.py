from fastapi import FastAPI, Request
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
# from another_mounted_app import sub_app

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:52175/'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=["Content-Disposition"],
)


@app.middleware("http")
async def cors_middleware(request: Request, call_next):
    if request.url.path == "/ws":
        # Exclude the /ws route from CORS headers
        response = await call_next(request)
    else:
        # Apply CORS headers for other routes
        response = await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
    return response


# @app.get("/ws")
# def read_root():
#     return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


from sockets import sio_app

app.mount('/', sio_app)

# app.mount("/mounted_app", sub_app)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=1111)



