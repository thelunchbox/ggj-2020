from rbt.game_components import map_entities
import pygame

class Material(map_entities.Map_Entities):
    def test(self):
        print(1)
    
    # Requires a position, and unique transistor ID       
    def __init__(self, pos, ID):
        super(Material, self).set_pos(pos, 'transistor')
        self.surface = pygame.Surface((30,30))
        self.surface.fill((163,255,15))
        self.ID = ID
        # The time it takes the transistor to regenerate its effect in milliseconds
        self.regenerationTime = 1000
        print('New transistor created with ID [' + self.ID + ' at:')
        print(self.pos[0:2])
        
    def render(self, screen):
        screen.blit(self.surface, self.pos)
        