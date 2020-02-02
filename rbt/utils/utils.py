import socket
import uuid

from constants import TILE_WIDTH, TILE_HEIGHT, MAP_BORDER

def getHostAddr():
    # hostname = socket.gethostname()
    # return socket.gethostbyname(hostname)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()
    return host

def getId():
    return str(uuid.uuid1())

def getClassName(x):
    return x.__class__.__name__


def screenCoords((x,y)):
    return ((TILE_WIDTH*x)+(MAP_BORDER/2),(TILE_HEIGHT*y)+(MAP_BORDER/2),TILE_WIDTH,TILE_HEIGHT)