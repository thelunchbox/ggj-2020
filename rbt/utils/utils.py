import socket
import uuid

from rbt.utils.constants import TILE_WIDTH, TILE_HEIGHT, MAP_BORDER

HALF_MAP_BORDER = MAP_BORDER/2

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


def screenCoords(coords):
    return ((TILE_WIDTH * coords[0]) + HALF_MAP_BORDER, (TILE_HEIGHT * coords[1]) + HALF_MAP_BORDER)


def mapCoords(coords):
    return ((coords[0] - HALF_MAP_BORDER) % TILE_WIDTH, (coords[1] - HALF_MAP_BORDER) % TILE_HEIGHT)