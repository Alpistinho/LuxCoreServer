from flask import request
from flask_restplus import Resource, fields

from ..server.instance import server
from ..state_machines.client_session_state_machine import client_session_machine

app, api = server.app, server.api
ns = api.namespace('config/', description='Operations related to render settings')

config_post_fields = api.model('Defining config', {'renderengine.type': fields.String})

@ns.route('/')
class RenderSettings(Resource):

	def __init__(self, api=None, *args, **kwargs):
		return super().__init__(api=api, *args, **kwargs)

	def get(self):
		"""
		Returns currently defined render configuration for this session
		"""
		return client_session_machine.current_configuration

	@api.expect(config_post_fields, validate = True)
	def post(self):
		"""
		Defines new render configuration for this session
		"""
		client_session_machine.update_configuration(request)

		return None, 201