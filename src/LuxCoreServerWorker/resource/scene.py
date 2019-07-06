from flask import request
from flask_restplus import Resource, fields

from ..server.instance import server
from ..state_machines.worker_machine import worker_machine

app, api = server.app, server.api
ns = api.namespace('scene/', description='Operations related to scene definition')


scene_post_fields = api.model('Defining scene', {'placeholder': fields.String})

@ns.route('/')
class SceneDefinition(Resource):

	def get(self):
		"""
		Returns currently defined scene definition for this session.
		"""
		return worker_machine.current_scene

	@api.expect(scene_post_fields, validate = True)
	def post(self):
		"""
		Defines new scene definition for this session.
		"""
		worker_machine.update_scene(request)

		return None, 201