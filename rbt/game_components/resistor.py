from rbt.game_components import map_entities
import pygame

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
        print('New resistor created with ID [' + self.ID + ' at:')
        print(self.pos[0:2])
        
    def render(self, screen):
        screen.blit(self.surface, self.pos)
        