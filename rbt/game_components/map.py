import pygame
from rbt.utils.constants import TILES
from rbt.utils.constants import TILE_PATHS
from rbt.utils.constants import MAP_WIDTH
from rbt.utils.constants import MAP_HEIGHT
from rbt.utils.constants import TILE_WIDTH
from rbt.utils.constants import TILE_HEIGHT
from rbt.utils.constants import MAP_BORDER, MAP_MARGIN
from rbt.game_components.tile import Tile
board = []


TILE_SURFACES = []
for file in TILE_PATHS:
    TILE_SURFACES.append(pygame.image.load(file))

class Map():
    def __init__(self):
        self.surface = pygame.Surface(((TILE_WIDTH * MAP_WIDTH)+MAP_BORDER , (TILE_HEIGHT * MAP_HEIGHT)+MAP_BORDER))
        self.surface.fill((220,220,220))
        self.generateMap(TILES)
        self.tiles = []

    def generateMap(self, tiles):
        for x in range(MAP_WIDTH):
            self.tiles.append([])
            for y in range(MAP_HEIGHT):
                #self.tiles[x].append(TILE_SURFACES[tiles[y][x]])
                self.tiles[x].append(Tile([tiles[y][x]], (x,y), {}})
                #self.surface.blit(self.board[x][y],((TILE_WIDTH*x)+(MAP_BORDER/2),(TILE_HEIGHT*y)+(MAP_BORDER/2),TILE_WIDTH,TILE_HEIGHT))

    def render(self, screen):
        screen.blit(self.surface, (MAP_MARGIN, 0))

    def update(self):
        pass

    def setFromState(self, state):
        pass

    def getState(self):
        pass

