from rbt.game_components import map_entities
import pygame

class Spawn(map_entities.Map_Entities):
    
    # Requires a position, unique spawn ID  
    def __init__(self, pos, id, value, player):
        super(Spawn, self).set_pos(pos, 'spawn')
        self.surface = pygame.Surface((30,30))
        self.surface.fill((168,30,20))
        self.id = id
        self.player = player
        print('New spawn created with ID [' + self.id + ' at:')
        print(self.pos[0:2])
        
    def render(self, screen):
        screen.blit(self.surface, self.pos)

    def getState(self):
        return {
            'pos': self.pos,
            'player': self.player
        }

    def update(self):
        pass
        
        