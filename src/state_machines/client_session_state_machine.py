from transitions import Machine

states = ['Unitialized',    # Needs to have configuration/scene provided
        'Configured',       # Configuration/scene was provided
        'Rendering',        # Currently rendering
        'Paused',           # Rendering is paused
        'Stopped', 			# Rendering was stopped. Results still available
        'Error'				# Configuration/scene is wrong
        ]

transitions = [
{ 'trigger': 'is_configured', 'source': 'Unitialized', 'dest': 'Configured' },
{ 'trigger': 'start_rendering', 'source': 'Configured', 'dest': 'Rendering' },
{ 'trigger': 'pause_rendering', 'source': 'Rendering', 'dest': 'Paused' },
{ 'trigger': 'stop_rendering', 'source': 'Rendering', 'dest': 'Stopped' },
{ 'trigger': 'stop_rendering', 'source': 'Paused', 'dest': 'Stopped' }
]

class Client_session_state_machine(object):


    def __init__(self, *args, **kwargs):

        self.machine = Machine(model=self, states=states, transitions=transitions, initial='Unitialized')

        self.current_configuration = None
        self.current_scene = None
        
        return super().__init__(*args, **kwargs)
    

    def update_configuration(self, config):
        self.current_configuration = config.json
        return

    def update_scene(self):
        self.current_configuration = config.json
        return
    