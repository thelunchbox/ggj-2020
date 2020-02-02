from rbt.game_components import map_entities
from rbt.utils.utils import screenCoords
import pygame

class Transistor(map_entities.Map_Entities):
    
    # Requires a position, and unique transistor ID       
    def __init__(self, pos, id, max):
        super(Transistor, self).set_pos(pos, 'Transistor')
        self.surface = pygame.Surface((32,32))
        self.surface.fill((163,255,15))
        self.id = id
        # This is the same as the transistor's value
        self.max = max
        self.tearDown = False
        print('New transistor created with ID [' + self.id + ' at:')
        print(self.pos[0:2])
        
    def render(self, screen):
        screen.blit(self.surface, screenCoords(self.pos))

    def getState(self):
        return {
            'pos': self.pos,
            'max': self.max,
            'type': self.type
        }

    def update(self):
        if (self.tearDown):
            print("Now destroying transistor " + self.id)
        