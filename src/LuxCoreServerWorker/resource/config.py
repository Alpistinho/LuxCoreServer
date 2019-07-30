import json
from collections import OrderedDict

from flask import request
from flask_restplus import Resource, fields

from ..server.instance import server
from ..state_machines.worker_machine import worker_machine
from .models.config_models import config_post_schema, config_schema_validator

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

	def post(self):
		"""
		Defines new render configuration for this session
		"""
		config_request = json.loads(request.get_data(as_text=True), object_pairs_hook=OrderedDict)
		config_schema_validator.validate(config_request)
		
		worker_machine.update_configuration(config_request)

		return None, 201

