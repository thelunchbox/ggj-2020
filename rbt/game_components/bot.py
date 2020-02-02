import pygame
import random
import operator
import os

from rbt.utils.constants import SIGNAL_DECAY, STARTING_TTL
from rbt.utils.utils import screenCoords

# This class represents the robots that the player controls

class Bot():

    def __init__(self, id, slots, owner):
        self.id = id
        self.image = None
        self.slots = slots
        self.speed = 3
        self.ttl = STARTING_TTL
        self.inventory = [] # tools i've picked up
        self.material = 0 # raw material
        self.owner = owner
        self.pos = (0,0)
        self.expired = False

    def set_pos(self, pos):
        self.pos = pos

    def set_color(self):
        sprite = 'Bluetooth_64.png' if self.owner == 1 else 'Redtooth_64.png'
        self.image = pygame.image.load(os.path.join('rbt', 'images', sprite))

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
        self.owner = botState['owner']
        
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
            self.expired = True

    def render(self, screen):
        if (self.image):
            screen.blit(self.image, screenCoords(self.pos))

    def interact(self, entity):
        pass
        