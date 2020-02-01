from rbt.game_components import map_entities
import pygame

class Capacitor(map_entities.Map_Entities):
    def test(self):
        print(1)
    
    # Requires a position, a capacitor value, and unique capacitor ID     
    def __init__(self, pos, ID, value):
        super(Capacitor, self).set_pos(pos, 'capacitor')
        self.surface = pygame.Surface((30,30))
        self.surface.fill((36,94,255))
        self.ID = ID
        # The time it takes the transistor to regenerate its effect in milliseconds
        self.value = value
        print('New transistor created with ID [' + self.ID + ' at:')
        print(self.pos[0:2])
        
    def render(self, screen):
        screen.blit(self.surface, self.pos)
        