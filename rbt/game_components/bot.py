import pygame
import random
import operator

# This class represents the robots that the player controls

class Bot():

    def __init__(self, botID, slots, owner):
        self.botID = botID
        self.image = pygame.Surface((30,30))
        self.slots = slots
        self.speed = 1
        self.ttl = 32000 #TODO: replace with config
        self.inventory = [] # tools i've picked up
        self.material = 0 # raw material
        self.owner = owner
        self.pos = (0,0)

    def set_pos(self, pos):
        self.pos = pos

    def set_color(self, color):
        print(color)
        self.image.fill(color)

    def getState(self):
        inventoryState = {}
        for t in self.inventory:
            inventoryState[t.toolID] = t.getState()

        return {
            'botID': self.botID,
            'slots': self.slots,
            'ttl': self.ttl,
            'inventory': inventoryState,
            'material': self.material,
            'pos': self.pos,
            'owner': self.owner
        }

    def setBotFromState(self, botState):
        self.slots = botState['slots']
        self.ttl = botState['ttl']
        self.material = botState['material']
        self.pos = botState['pos']
        
        #TODO: set inventory from state

    def move(self):
        #TODO : write better moving logic
        if self.owner == 1:
            self.pos = tuple(map(operator.add, self.pos, (0, self.speed)))
        else:
            self.pos = tuple(map(operator.sub, self.pos, (0, self.speed)))

    def update(self):
        self.move()

    def render(self, screen):
        screen.blit(self.image, self.pos)
        