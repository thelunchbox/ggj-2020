import pygame
from rbt.utils.constants import TILES
from rbt.utils.constants import TILE_PATHS
from rbt.utils.constants import MAP_WIDTH
from rbt.utils.constants import MAP_HEIGHT
from rbt.utils.constants import TILE_WIDTH
from rbt.utils.constants import TILE_HEIGHT
from rbt.utils.constants import MAP_BORDER
from rbt.utils.constants import SPAWN_POINTS
from rbt.utils.utils import screenCoords, mapCoords, getId, getClassName
from rbt.game_components.tile import Tile
from rbt.game_components.spawn import Spawn
board = []


TILE_SURFACES = []
for file in TILE_PATHS:
    TILE_SURFACES.append(pygame.image.load(file))

class Map():
    def __init__(self):
        self.surface = pygame.Surface(((TILE_WIDTH * MAP_WIDTH)+MAP_BORDER , (TILE_HEIGHT * MAP_HEIGHT)+MAP_BORDER))
        self.surface.fill((220,220,220))
        self.tiles = []
        self.generateMap(TILES)

    def generateMap(self, tiles):
        for x in range(MAP_WIDTH):
            self.tiles.append([])
            for y in range(MAP_HEIGHT):
                self.tiles[x].append(Tile(tiles[y][x], (x,y), {}))
                self.surface.blit(self.tiles[x][y].getBackground(), screenCoords((x,y)))
        self.initializeSpawns()

    def initializeSpawns(self):
        for sp in SPAWN_POINTS:
            t = sp[0]
            owner = sp[1]
            tile = self.tiles[t[0]][t[1]]
            spawn = Spawn(t, getId(), owner)
            tile.addEntity(spawn)

    def isSpawn(self, t, p):
        tile = self.tiles[t[0]][t[1]]
        spawn = tile.contains('Spawn')
        if not spawn:
            return False
        else:
            print(spawn.player, p)
            return spawn.player == p

    def render(self, screen):
        screen.blit(self.surface, (0, 0))
        mouseCoords = pygame.mouse.get_pos()
        mapMouseCoords = mapCoords(mouseCoords)
        for x in range(MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                hover = mapMouseCoords[0] == x and mapMouseCoords[1] == y
                self.tiles[x][y].render(screen, hover)
                
    def update(self):
        for x in range(MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                tile = self.tiles[x][y]
                tile.update()

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
                mapState[x].append(tile.getState())
        return {
            'map': mapState
        }
            

