from flask import request
from flask_restplus import Resource, fields

from ..server.instance import server
from ..state_machines.client_session_state_machine import client_session_machine

app, api = server.app, server.api
ns = api.namespace('scene/', description='Operations related to scene definition')

@ns.route('/')
class SceneDefinition(Resource):

	def get(self):
		"""
		Returns currently defined scene definition for this session.
		"""
		return client_session_machine.current_configuration

	def post(self):
		"""
		Defines new scene definition for this session.
		"""
		client_session_machine.update_scene(request)

		return None, 201