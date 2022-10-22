import socketio
import uvicorn

import utils.constants as constants
from game.game_namespace import GameNamespace


if __name__ == "__main__":
    sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
    sio.register_namespace(GameNamespace("/"))
    app = socketio.ASGIApp(sio)
    uvicorn.run(app, host=constants.HOST, port=constants.LISTENER_PORT)