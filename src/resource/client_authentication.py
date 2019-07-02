from flask import request, jsonify
from flask_restplus import Resource, fields, marshal_with
from flask_jwt_extended import JWTManager, create_access_token

from src.server.instance import server
from src.authentication.client_authentication_shared import jwt, connected_clients

app, api = server.app, server.api
ns = api.namespace('client/', description='Operations related to client authentication')

client_registration_fields = api.model('Client registration', {'username': fields.String})

@ns.route('/register')
class ClientRegistration(Resource):
	
	@api.expect(client_registration_fields, validate = True)
	@api.doc(responses={406: 'Not Acceptable'})
	@api.doc(responses={201: 'Client registered'})
	def post(self):
		"""
		Creates new user using provided username and password
		"""
		username = request.json.get('username', None)

		if username in connected_clients:
			return {'message': 'Client already registered'}, 406

		
		access_token = create_access_token(identity=username)
		connected_clients[username] = access_token

		return {'access_token': access_token}, 201