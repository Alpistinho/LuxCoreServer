from flask import request, jsonify
from flask_restplus import Resource, fields

from ..server.instance import server
from ..state_machines.worker_machine import worker_machine

app, api = server.app, server.api
ns = api.namespace('rendering/', description='Operations related to rendering control')

config_post_fields = api.model('Defining config', {'renderengine.type': fields.String})

@ns.route('/start')
class StartRendering(Resource):

	def __init__(self, api=None, *args, **kwargs):
		return super().__init__(api=api, *args, **kwargs)

	def start_rendering(self):

		worker_machine.start_rendering()
		return

	def get(self):
		"""
		Starts rendering if scene is correctly configured
		"""
		print('Worker state: ', worker_machine.state)
		if worker_machine.is_configured():
			self.start_rendering()
		
		else:
			return {'message:': 'Scene must be configured before starting rendering'}, 406

		return None, 201