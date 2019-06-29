import uuid

from flask import Flask
from flask_restplus import Api, Resource, fields

from src.environment.instance import environment_config

class Client(object):
    def __init__(self, username, password):
        self.id = uuid.uuid4()
        self.username = username
        self.password = password

class Server(object):
	def __init__(self):
		self.app = Flask(__name__)
		self.api = Api(self.app,
					  version='0.1', 
					  title='LuxCoreServer REST API', 
					  description='API for defining LuxCore scenes, render settings and controlling the rendering process',
					  doc = environment_config["swagger-url"])

		self.app.config['SECRET_KEY'] = 'super-secret'

	def run(self):
		self.app.run(
				debug = environment_config["debug"], 
				port = environment_config["port"]
			)

server = Server()