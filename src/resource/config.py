from flask import request
from flask_restplus import Resource

from src.server.instance import server

app, api = server.app, server.api
ns = api.namespace('session/', description='Operations related to render settings')

@ns.route('config')
class RenderSettings(Resource):

	def __init__(self, api=None, *args, **kwargs):
		print('RenderSettings')
		return super().__init__(api=api, *args, **kwargs)


	def get(self):
		"""
		Returns currently defined render configuration for this session
		"""
		return "Hello2"

	def post(self):
		"""
		Defines new render configuration for this session
		"""
		data = request.json
		return None, 201