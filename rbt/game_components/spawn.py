from rbt.game_components import map_entities
from rbt.utils.utils import screenCoords
import pygame

class Spawn(map_entities.Map_Entities):
    
    # Requires a position, unique spawn ID  
    def __init__(self, pos, id, value, player):
        super(Spawn, self).set_pos(pos, 'Spawn')
        self.surface = pygame.Surface((30,30))
        self.surface.fill((168,30,20))
        self.id = id
        self.player = player
        print('New spawn created with ID [' + self.id + ' at:')
        print(self.pos[0:2])
        
    def render(self, screen):
        screen.blit(self.surface, screenCoords(self.pos))

    def getState(self):
        return {
            'pos': self.pos,
            'player': self.player,
            'type': self.type
        }

    def update(self, tile):
        pass

    def clean(self):
        pass
        