from transitions import Machine

class Client_session_state_machine():

    states = ['Unitialized', 'Available']
    transitions = [
    { 'trigger': 'Initialize', 'source': 'Unitialized', 'dest': 'Available' }
    ]

    def __init__(self, *args, **kwargs):

        self.machine = Machine(model=self, states=LuxCoreServer_state_machine.states, transitions=transitions, initial='Unitialized')
        return super().__init__(*args, **kwargs)
    
    def Initalize(self):
        return