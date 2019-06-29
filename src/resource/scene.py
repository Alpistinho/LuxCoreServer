from flask import request
from flask_restplus import Resource

from src.server.instance import server

app, api = server.app, server.api
ns = api.namespace('session/', description='Operations related to scene definition')

@ns.route('/scene')
class SceneDefinition(Resource):

	def get(self):
		"""
		Returns currently defined scene definition for this session.
		"""
		return "0"

	def post(self):
		"""
		Defines new scene definition for this session.
		"""
		return None, 201