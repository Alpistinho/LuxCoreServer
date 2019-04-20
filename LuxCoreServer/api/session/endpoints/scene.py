from flask import request
from flask_restplus import Resource

from api.restplus import luxCoreServerApi

from luxcore_integration import render_session

ns = luxCoreServerApi.namespace('session/scene', description='Operations related to scene definition')

@ns.route('/')
class SceneDefinition(Resource):

	def get(self):
		"""
		Returns currently defined scene definition for this session.
		"""
		return render_session.session0.get_scene()

	def post(self):
		"""
		Defines new scene definition for this session.
		"""
		render_session.session0.set_scene(request)
		return None, 201