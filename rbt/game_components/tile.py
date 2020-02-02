import pygame
from rbt.utils.utils import getClassName

from rbt.game_components.bot import Bot

class Tile():
    def __init__(self, config, entities):
        self.surface = pygame.image.load(config.tileImage)
        self.openPaths = config.openPaths
        self.gameEntities = entities # this is a dictionary

    def addEntity(self, entity):
        self.gameEntities[entity.id] = entity
    
    def removeEntity(self, entity):
        del self.gameEntities[entity.id]
    
    def checkCollisions(self):
        for a in self.gameEntities.values():
            for b in self.gameEntities.values():
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
    
    def render(self, screen):
        for entity in self.gameEntities:
            entity.render(screen)

    def setFromState(self, state):
        entityStates = state['entities']

        # create new entities
        for id in entityStates.keys():
            if (not self.gameEntities.get(id, None)):
                entityState = entityStates[id]
                entityType = entityState['type']
                if (entityType == 'Bot'):
                    bot = Bot(id, entityState['slots'], entityState['owner'])
                    bot.set_color((0,255,0)) # fix pls
                    self.addEntity(bot)
        
        # update/delete entities
        for id in self.gameEntities.keys():
            if (not entityStates.get(id, False)):
                self.removeEntity(self.gameEntities[id])
            else:
                self.gameEntities[id].setFromState(entityStates[id])

    def update(self):
        for entity in self.gameEntities.values():
            entity.update()

        for entity in self.gameEntities.values():
            if (entity.expired):
                self.removeEntity(entity)

    def getState(self):
        entityStates = {}
        for entity in self.gameEntities.values():
            entityStates[entity.id] = entity.getState()

    def getExit(self):
        pass
