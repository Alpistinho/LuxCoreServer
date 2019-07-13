from flask import request
from flask_restplus import Resource, fields

from ..server.instance import server
from ..state_machines.worker_machine import worker_machine
from .models.config_models import config_post_model

app, api = server.app, server.api
ns = api.namespace('config/', description='Operations related to render configuration settings')

@ns.route('/')
class RenderSettings(Resource):

	def __init__(self, api=None, *args, **kwargs):
		return super().__init__(api=api, *args, **kwargs)

	def get(self):
		"""
		Returns currently defined render configuration for this session
		"""
		return worker_machine.current_configuration

	# @api.marshal_with(config_post_model, as_list=True)
	@api.expect(config_post_model, validate = True)
	def post(self):
		"""
		Defines new render configuration for this session
		"""
		worker_machine.update_configuration(request)

		return None, 201

