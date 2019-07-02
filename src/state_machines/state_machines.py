from src.state_machines.client_session_state_machine import *

_client_state_machines = {}

def get_client_state_machine_by_identity(current_identity):
    if not(current_identity):
        current_identity = 'test_user'

    if current_identity in _client_state_machines:
        client_state_machine = _client_state_machines[current_identity]
    else:
        client_state_machine = Client_session_state_machine()
        _client_state_machines[current_identity] = client_state_machine

    return client_state_machine
