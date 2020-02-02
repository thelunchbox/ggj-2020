import pygame
from rbt.utils.utils import getClassName

class Tile():
    def __init__(self, config, entities):
        self.surface = pygame.image.load(config.tileImage)
        self.openPaths = config.openPaths
        self.gameEntities = entities

    def addEntity(self, entity):
        self.gameEntities.append(entity)
    
    def removeEntity(self, entity):
        self.gameEntities.remove(entity)
    
    def checkCollisions(self):
        for a in self.gameEntities:
            for b in self.gameEntities:
                if (a.id != b.id): # not the same id means it's not the same entity
                    aIsBot = getClassName(a) == 'Bot'
                    bIsBot = getClassName(b) == 'Bot'
                    if (aIsBot and bIsBot):
                        # do battle
                        pass
                    elif (aIsBot):
                        a.interact(b)
                    elif (bIsBot):
                        b.interact(a)
    
    def render(self):
        pass

    def setTileFromState(self):
        pass

    def update(self):
        pass
    
    def getState(self):
        pass

    def getExit(self):
        pass
