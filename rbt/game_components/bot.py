import pygame
import random
import operator

from rbt.utils.constants import SIGNAL_DECAY

# This class represents the robots that the player controls

class Bot():

    def __init__(self, id, slots, owner):
        self.id = id
        self.image = pygame.Surface((30,30))
        self.slots = slots
        self.speed = 3
        self.ttl = 32000 #TODO: replace with config
        self.inventory = [] # tools i've picked up
        self.material = 0 # raw material
        self.owner = owner
        self.pos = (0,0)
        self.dead = False

    def set_pos(self, pos):
        self.pos = pos

    def set_color(self, color):
        self.image.fill(color)

    def getState(self):
        inventoryState = {}
        for t in self.inventory:
            inventoryState[t.id] = t.getState()

        return {
            'id': self.id,
            'type': 'Bot',
            'slots': self.slots,
            'ttl': self.ttl,
            'inventory': inventoryState,
            'material': self.material,
            'pos': self.pos,
            'owner': self.owner
        }

    def setFromState(self, botState):
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
        self.ttl -= SIGNAL_DECAY
        if (self.ttl <= 0):
            self.dead = True
        if (self.pos[1] > 1020 or self.pos[1] < 0): #TODO: fix me
            self.dead = True

    def render(self, screen):
        screen.blit(self.image, self.pos)

    def interact(self, entity):
        pass
        