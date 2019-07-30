from flask_restplus import fields

from ...server.instance import server

api = server.api
scene_post_model = api.model('Scene_definition', {'placeholder': fields.String})