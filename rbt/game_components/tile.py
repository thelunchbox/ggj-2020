import pygame, random
from rbt.utils.utils import getClassName
from rbt.utils.constants import TILE_PATHS, TILE_EXITS, COLOR
from rbt.game_components.bot import Bot
from rbt.game_components.spawn import Spawn
from rbt.utils.utils import screenCoords

class Tile():
    def __init__(self, index, pos, map, entities):
        self.surface = pygame.image.load(TILE_PATHS[index])
        self.exits = TILE_EXITS[index]
        self.gameEntities = entities # this is a dictionary
        self.pos = pos
        self.map = map
        self.removeList = []

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
                        a.interact(b, getClassName(b))
                    elif (bIsBot):
                        b.interact(a, getClassName(a))
    
    def render(self, screen, hover):
        for entity in self.gameEntities.values():
            entity.render(screen)
        if hover:
            xy = screenCoords(self.pos)
            pygame.draw.rect(screen, COLOR['cyan'], (xy[0], xy[1], 64, 64), 2)

    def getBackground(self):
        return self.surface

    # look for entities
    def contains(self, entityType):
        for x in self.gameEntities.values():
            if getClassName(x) == entityType:
                return x
        return None

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
        self.removeList = []
        for entity in self.gameEntities.values():
            entity.clean()

        for entity in self.gameEntities.values():
            entity.update(self)

        for entity in self.gameEntities.values():
            if (entity.expired):
                self.removeList.append(entity.id)

        for key in set(self.removeList):
                self.removeEntity(self.gameEntities[key])

    def getState(self):
        entityStates = {}
        for entity in self.gameEntities.values():
            entityStates[entity.id] = entity.getState()
        return {
            'entities': entityStates
        }

    def getDirection(self, targetPos):
        if self.exits:
            exitDirection = random.choice(self.exits)
            print (exitDirection)
            return exitDirection
        return 'None'

    def moveEntity(self, entity, direction):
        targetTile = None
        if(direction == "north"):
            targetTile =self.map.getTile((self.pos[0], self.pos[1]-1))
        elif(direction == "south"):
            targetTile =self.map.getTile((self.pos[0], self.pos[1]+2))
        elif(direction == "east"):
            targetTile =self.map.getTile((self.pos[0]+1, self.pos[1]))
        else:
            targetTile =self.map.getTile((self.pos[0]-1, self.pos[1]))
        if targetTile:
            targetTile.addEntity(entity)
            self.removeList.append(entity.id)

