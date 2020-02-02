from rbt.game_components import map_entities
import pygame
from rbt.utils.constants import CAPACITANCE_DRAIN

class Capacitor(map_entities.Map_Entities):
    
    # Requires a position, a capacitor value, and unique capacitor ID     
    def __init__(self, pos, ID, max):
        super(Capacitor, self).set_pos(pos, 'Capacitor')
        self.surface = pygame.Surface((30,30))
        self.surface.fill((36,94,255))
        self.ID = ID
        # The current amount of charge available in the capacitor
        self.value = max
        # The maximum capacitance of the capacitor
        self.max = max
        self.tearDown = False
        print('New transistor created with ID [' + self.ID + ' at:')
        print(self.pos[0:2])

        self.draining = False
        
    def render(self, screen):
        screen.blit(self.surface, self.pos)

    def getState(self):
        return {
            'pos': self.pos,
            'capacitance': self.value,
            'type': self.type
        }

    def update(self):
        if (self.draining):
            self.value -= CAPACITANCE_DRAIN
        elif (self.value < self.max):
            self.value += CAPACITANCE_DRAIN
            if (self.value > self.max): # whoops we might have gone past
                self.value = self.max
        if (self.tearDown):
            print("Now destroying capacitor " + self.ID)
        