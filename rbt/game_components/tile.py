import pygame
from rbt.utils.utils import getClassName
from rbt.utils.constants import TILE_PATHS, TILE_EXITS, COLOR
from rbt.game_components.bot import Bot
from rbt.game_components.spawn import Spawn
from rbt.utils.utils import screenCoords

class Tile():
    def __init__(self, index, pos, entities):
        self.surface = pygame.image.load(TILE_PATHS[index])
        self.exits = TILE_EXITS[index]
        self.gameEntities = entities # this is a dictionary
        self.pos = pos

    def addEntity(self, entity):
        self.gameEntities[entity.id] = entity
        entity.pos = self.pos
    
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
    
    def render(self, screen, hover):
        if hover:
            xy = screenCoords(self.pos)
            pygame.draw.rect(screen, COLOR['cyan'], (xy[0], xy[1], 64, 64), 2)

        for entity in self.gameEntities.values():
            print('rendering entity', getClassName(entity), entity.id)
            entity.render(screen)

    def getBackground(self):
        return self.surface

    def setFromState(self, state):
        entityStates = state['entities']
        # create new entities
        for id in entityStates.keys():
            if (not self.gameEntities.get(id, None)):
                entityState = entityStates[id]
                entityType = entityState['type']
                if (entityType == 'Bot'):
                    bot = Bot(id, entityState['slots'], entityState['owner'])
                    bot.set_color()
                    self.addEntity(bot)
                if (entityType == 'Spawn'):
                    spawn = Spawn(self.pos, id, entityState['player'])
                    self.addEntity(spawn)

        destroyedEntityIds = []
        # update/delete entities
        for id in self.gameEntities.keys():
            if (not entityStates.get(id, False)):
                destroyedEntityIds.append(id)
            else:
                self.gameEntities[id].setFromState(entityStates[id])

        for key in destroyedEntityIds:
                self.removeEntity(self.gameEntities[key])

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
        return {
            'entities': entityStates
        }

    def getExit(self):
        pass
