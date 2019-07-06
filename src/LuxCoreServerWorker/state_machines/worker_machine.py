from transitions import Machine

from .lib import pyluxcore

states = ['unitialized',    # Needs to have configuration/scene provided
		'configured',       # Configuration/scene was provided
		'rendering',        # Currently rendering
		'paused',           # Rendering is paused
		'stopped', 			# Rendering was stopped. Results still available
		'error'				# Configuration/scene is wrong
		]

transitions = [
{ 'trigger': 'set_configured', 'source': ['unitialized','configured'], 'dest': 'configured' },
{ 'trigger': 'start_rendering', 'source': 'configured', 'dest': 'rendering' },
{ 'trigger': 'pause_rendering', 'source': 'rendering', 'dest': 'paused' },
{ 'trigger': 'stop_rendering', 'source': ['rendering', 'paused'], 'dest': 'stopped' }
]

class Worker_machine(object):


	def __init__(self, *args, **kwargs):

		self.machine = Machine(model=self, states=states, transitions=transitions, initial='unitialized')

		self.current_configuration = None
		self.current_scene = None

		self._init_pyluxcore()
		self._session = None
		
		return super().__init__(*args, **kwargs)

	def _init_pyluxcore(self):
		pyluxcore.Init()
		self.props = pyluxcore.Properties()
		self.scene = pyluxcore.Scene()

		return
	
	def _set_props(self):
		print('Setting props')
		for key, value in self.current_configuration:
			print(key, value)
		return
	
	def _set_scene(self):
		return

	def start_rendering(self):

		self._set_props()
		self._set_scene()
		# self.config = pyluxcore.RenderConfig(self.props, self.scene)

  		# # Create the rendering session
		# self._session = pyluxcore.RenderSession(self.config)
		# # Start the rendering
		# self._session.Start()
	
	def check_if_configured(self):
		if (self.current_configuration is not None and self.current_scene is not None):
			self.set_configured()

		return self.is_configured()

	def update_configuration(self, config):
		self.current_configuration = config.json
		self.check_if_configured()
		return

	def update_scene(self, scene):
		self.current_scene = scene.json
		self.check_if_configured()
		return
	
worker_machine = Worker_machine()