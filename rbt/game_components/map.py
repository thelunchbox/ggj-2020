import pygame
from rbt.utils.constants import TILES
from rbt.utils.constants import TILE_PATHS
from rbt.utils.constants import MAP_WIDTH
from rbt.utils.constants import MAP_HEIGHT
#from rbt.utils.constants import TILE_WIDTH
#from rbt.utils.constants import TILE_HEIGHT
board = []


TILE_SURFACES = []
for file in TILE_PATHS:
    TILE_SURFACES.append(pygame.image.load(file))

# if we want to just discover the width and height of the tiles
s = TILE_SURFACES[0].get_rect()
TILE_WIDTH  = s.width
TILE_HEIGHT = s.height

class Tile():
    def __init__(self, config, entities):
        self.surface = pygame.image.load(config.tileImage)
        self.openPaths = config.openPaths
        self.gameEntities = entities

class Map():
    def __init__(self):
        self.surface = pygame.Surface((TILE_WIDTH * MAP_WIDTH, TILE_HEIGHT * MAP_HEIGHT))
        self.setBoard()

    def setBoard(self):
        self.board       = []
        for x in range(MAP_WIDTH):
            self.board.append([])
            for y in range(MAP_HEIGHT):
                self.board[x].append(TILE_SURFACES[TILES[x][y]])
                self.surface.blit(self.board[x][y],(TILE_WIDTH*x,TILE_HEIGHT*y,TILE_WIDTH,TILE_HEIGHT))

    def render(self, screen):
        screen.blit(self.surface, (0,0))

