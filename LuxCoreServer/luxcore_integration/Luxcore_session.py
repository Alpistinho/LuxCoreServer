from luxcore_integration.lib import pyluxcore


class Luxcore_session():
    def __init__(self, *args, **kwargs):
        pyluxcore.Init()
        self.scene = ''
        return super().__init__(*args, **kwargs)

    def set_scene(self, scene):
        self.scene = scene
    
    def get_scene(self):
        return self.scene

session0 = Luxcore_session()