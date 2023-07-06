import socketio
import asyncio

sio = socketio.AsyncClient()


async def connect():
    headers = {
        "token": "dataa121asdadsassda",
        "session_id": "your_session_id",
        "client_id": "your_client_id"
    }
    await sio.connect('http://localhost:1111', auth={
        "session_id": "333dsa",
        "retailer_id": "222",
        "client_id": "111",
        "user_id": "1234"
    }, wait_timeout=30, headers=headers)


@sio.on('connect')
async def on_connect():
    print('Connected to server')


@sio.on('chat')
def on_chat(data):
    print('Received message:', data)


@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')


async def main():
    await connect()

    await sio.emit('query', 'Hello, server!, from client')

    await asyncio.sleep(1)

    await sio.disconnect()


if __name__ == '__main__':
    asyncio.run(main())
