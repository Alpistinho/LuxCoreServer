from flask_restplus import fields

from ...server.instance import server

api = server.api
config_post_model = api.model('Render configuration model',
 {'renderengine.type': fields.String,
 'int': fields.Integer,
 'listInts': fields.List(fields.Integer)})