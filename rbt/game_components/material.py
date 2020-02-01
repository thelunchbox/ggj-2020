from rbt.game_components import map_entities
import pygame

class Material(map_entities.Map_Entities):
    def test(self):
        print(1)
    
    # Requires a position, unique material ID and a value (number of material units)    
    def __init__(self, pos, ID, value):
        super(Material, self).set_pos(pos, 'material')
        self.surface = pygame.Surface((30,30))
        self.surface.fill((255,255,51))
        self.ID = ID
        self.value = value
        print('New material created with ID [' + self.ID + ' at:')
        print(self.pos[0:2])
        
    def render(self, screen):
        screen.blit(self.surface, self.pos)
        