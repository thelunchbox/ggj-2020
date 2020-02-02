from rbt.game_components import map_entities
import pygame
from rbt.utils.constants import RESISTOR_DAMAGE

class Resistor(map_entities.Map_Entities):
    def test(self):
        print(1)
    
    # Requires a position, unique Resistor ID and a value (number of Resistor units)    
    def __init__(self, pos, ID, value):
        super(Resistor, self).set_pos(pos, 'resistor')
        self.surface = pygame.Surface((30,30))
        self.surface.fill((168,30,20))
        self.ID = ID
        # This value is compared to the Gremlin's TTL (avg 32000?)
        self.value = value
        self.tearDown = False
        print('New resistor created with ID [' + self.ID + ' at:')
        print(self.pos[0:2])

        self.destroying = False
        
    def render(self, screen):
        screen.blit(self.surface, self.pos)

    def getState(self):
        if (self.value <= 0):
            return None # this means we are destroyed
        else:
            return {
                'pos': self.pos,
                'resistance': self.value
            }

    def update(self):
        if (self.destroying):
            self.value -= RESISTOR_DAMAGE
        if (self.tearDown):
            print("Now destroying resistor " + self.ID)
        
        