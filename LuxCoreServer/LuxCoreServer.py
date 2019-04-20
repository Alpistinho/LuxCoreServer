import os

from flask import Flask, Blueprint

from api.restplus import luxCoreServerApi
from api.session.endpoints.scene import ns as scene_namespace
from api.session.endpoints.config import ns as config_namespace

from luxcore_integration import render_session

import settings



app = Flask(__name__)

def configure_app(flask_app):
	flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME

def initialize_app(flask_app):
	configure_app(flask_app)
	blueprint = Blueprint('api', __name__)
	luxCoreServerApi.init_app(blueprint)
	luxCoreServerApi.add_namespace(scene_namespace)
	luxCoreServerApi.add_namespace(config_namespace)
	flask_app.register_blueprint(blueprint)



def main():
	initialize_app(app)
	session = render_session.Render_session()
	app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
	main()
