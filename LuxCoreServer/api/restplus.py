from flask_restplus import Api

luxCoreServerApi = Api(version='0.1', title='LuxCoreServer REST API', description='API for defining LuxCore scenes, render settings and controlling the rendering process')


@luxCoreServerApi.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'

