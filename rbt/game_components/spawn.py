from rbt.game_components import map_entities
from rbt.utils.utils import screenCoords
import pygame

class Spawn(map_entities.Map_Entities):
    
    # Requires a position, unique spawn ID  
    def __init__(self, pos, id, player):
        super(Spawn, self).set_pos(pos, 'Spawn')
        self.surface = pygame.Surface((32,32))
        self.surface.fill((168,30,20))
        self.id = id
        self.player = player
        self.expired = False
        
    def render(self, screen):
        screen.blit(self.surface, screenCoords(self.pos))

    def getState(self):
        return {
            'pos': self.pos,
            'player': self.player,
            'type': self.type
        }
    
    def setFromState(self, state):
        pass

    def update(self):
        pass
        
        