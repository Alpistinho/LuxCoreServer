from .server.instance import server

from .resource.scene import *
from .resource.config import *
from .resource.rendering import *

if __name__ == '__main__':
    server.run()