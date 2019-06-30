from flask_jwt_extended import JWTManager

from src.server.instance import server
app, api = server.app, server.api

jwt = JWTManager(app)

_connected_clients = {}