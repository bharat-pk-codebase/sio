from fastapi import FastAPI
from fastapi_socketio import SocketManager

app = FastAPI()
socket_manager = SocketManager(app=app)


from fastapi import FastAPI
import uvicorn
from sockets import sio_app
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from typing import Union



@app.get("/ws")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
#
#
# if __name__ == '__main__':
#     uvicorn.run("main:app", reload=True, port=1111)
