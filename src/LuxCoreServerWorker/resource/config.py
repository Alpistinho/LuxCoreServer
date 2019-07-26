import json
from collections import OrderedDict

from flask import request
from flask_restplus import Resource, fields

from ..server.instance import server
from ..state_machines.worker_machine import worker_machine
from .models.config_models import config_post_model

app, api = server.app, server.api
ns = api.namespace('config/', description='Operations related to render configuration settings', ordered=True)

@ns.route('/')
class RenderSettings(Resource):

	def __init__(self, api=None, *args, **kwargs):
		return super().__init__(api=api, *args, **kwargs)

	def get(self):
		"""
		Returns currently defined render configuration for this session
		"""
		return worker_machine.current_configuration

	@ns.expect(config_post_model, validate = True, ordered=True)
	def post(self):
		"""
		Defines new render configuration for this session
		"""
		# print(dir(request))
		print(request.data)
		print(type(request.data))
		config = json.loads(request.get_data(as_text=True), object_pairs_hook=OrderedDict)
		worker_machine.update_configuration(config)

		return None, 201

