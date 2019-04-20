import uuid

from luxcore_integration import Luxcore_session

class Session_control():
    def __init__(self):
        self.sessions = {}
        return
    
    def create_new_session(self):
        session_id = uuid.uuid4.hex
        self.sessions[session_id] = Luxcore_session()
    
    def get_session(self, session_id):
        return self.sessions[session_id]