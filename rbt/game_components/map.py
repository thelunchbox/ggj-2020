import pygame
from rbt.utils.constants import TILES
from rbt.utils.constants import TILE_PATHS
from rbt.utils.constants import MAP_WIDTH
from rbt.utils.constants import MAP_HEIGHT
from rbt.utils.constants import TILE_WIDTH
from rbt.utils.constants import TILE_HEIGHT
from rbt.utils.constants import MAP_BORDER, MAP_MARGIN
from rbt.utils.utils import screenCoords
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
                self.tiles[x].append(Tile([tiles[y][x]], (x,y), {}})
                self.surface.blit(self.tiles[x][y].getBackground(), screenCoords((x,y))

    def render(self, screen):
        screen.blit(self.surface, (0, 0))

        for x in range(MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                tiles[x][y].render(screen)

    def update(self):
        pass

    def setFromState(self, state):
        mapState = state['map']
        for x in range(MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                tile = self.tiles[x][y]
                tile.setFromState(mapState[x][y])

    def getState(self):
        mapState = []
        for x in range(MAP_WIDTH):
            mapState.append([])
            for y in range(MAP_HEIGHT):
                tile = self.tiles[x][y]
                mapState.append(tile.getState())
        return {
            'map': mapState
        }
            

