import socketio
from fastapi import Depends, HTTPException, status

sio_server = socketio.AsyncServer(async_mode='asgi',
                                  cors_allowed_origins='*')

sio_app = socketio.ASGIApp(socketio_server=sio_server,
                           # socketio_path="sockets"
                           )

active_connections = []


@sio_server.event
async def connect(sid, environ, auth):
    print(f'connected auth={auth} sid={sid}')
    active_connections.append(sid)
    headers_dict = {key.decode(): value.decode() for key, value in environ["asgi.scope"]["headers"]}
    print(headers_dict)

    print(f"Active connections:- {str(active_connections)}")
    await sio_server.emit('chat', {'data': 'Connected', 'sid': sid}, room=sid)


# async def verify_token(token: str) -> bool:
#     if token == "dataa121asdadsassda":
#         return True
#     return False
#
#
# @sio_server.event
# async def connect(sid, environ, auth):
#     print(f'connected auth={auth} sid={sid}')
#     print(f"Active connections:- {str(active_connections)}")
#     active_connections.append(sid)
#     token = auth.get("token")
#     if not await verify_token(token):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
#     await sio_server.emit('chat', {'data': 'Connected', 'sid': sid}, room=sid)


@sio_server.event
def disconnect(sid):
    print('disconnected', sid)
    active_connections.remove(sid)
    print(f"Active connections:- {str(active_connections)}")


@sio_server.on('query')
async def test_message(sid, message):
    print(message)
    await sio_server.emit('chat', {'data': message + " -Interaction Engine"}, room=sid)

# server --> query
#
# client --> chat
