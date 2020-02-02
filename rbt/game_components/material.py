from rbt.game_components import map_entities
import pygame

class Material(map_entities.Map_Entities):
    
    # Requires a position, unique material ID and a value (number of material units)    
    def __init__(self, pos, id, value):
        super(Material, self).set_pos(pos, 'Material')
        self.surface = pygame.Surface((30,30))
        self.surface.fill((255,255,51))
        self.id = id
        self.value = value
        self.tearDown = False
        print('New material created with ID [' + self.id + ' at:')
        print(self.pos[0:2])
        
    def render(self, screen):
        screen.blit(self.surface, self.pos)
        
    def getState(self):
        return {
            'pos': self.pos,
            'value': self.value,
            'type': self.type
        }
        
    def update(self):
        if (self.tearDown):
            print("Now destroying material " + self.id)
        