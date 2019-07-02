from flask import request
from flask_restplus import Resource, fields
from flask_jwt_extended import jwt_optional, get_jwt_identity

from src.server.instance import server
from src.state_machines.state_machines import get_client_state_machine_by_identity
from src.authentication.client_authentication_shared import jwt

app, api = server.app, server.api
ns = api.namespace('scene/', description='Operations related to scene definition')

@ns.route('/')
class SceneDefinition(Resource):

	@jwt_optional
	def get(self):
		"""
		Returns currently defined scene definition for this session.
		"""
		client_state_machine = get_client_state_machine_by_identity(get_jwt_identity())
		return client_state_machine.current_configuration

	@jwt_optional
	def post(self):
		"""
		Defines new scene definition for this session.
		"""
		client_state_machine = get_client_state_machine_by_identity(get_jwt_identity())
		client_state_machine.update_configuration(request)

		return None, 201