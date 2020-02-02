import socket
import uuid
from datetime import datetime

from rbt.utils.constants import TILE_WIDTH, TILE_HEIGHT, MAP_BORDER, TOOL_BUTTON_WIDTH, TOOL_BUTTON_HEIGHT

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
    return (int((coords[0] - HALF_MAP_BORDER) / TILE_WIDTH), int((coords[1] - HALF_MAP_BORDER) / TILE_HEIGHT))

def isOver(buttonPos, pos):
    #Pos is the mouse position or a tuple of (x,y) coordinates
    if pos[0] > buttonPos[0] and pos[0] < buttonPos[0] + TOOL_BUTTON_WIDTH:
        if pos[1] > buttonPos[1] and pos[1] < buttonPos[0] + TOOL_BUTTON_HEIGHT:
            return True
    return False

def ticks(dt):
    return (dt - datetime(1, 1, 1)).total_seconds() * 10000000