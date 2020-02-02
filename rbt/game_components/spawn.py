from rbt.game_components import map_entities
from rbt.utils.utils import screenCoords
import pygame

class Spawn(map_entities.Map_Entities):
    
    # Requires a position, unique spawn ID  
    def __init__(self, pos, id, player):
        super(Spawn, self).set_pos(pos, 'Spawn')
        self.surface = pygame.Surface((64,64))
        self.surface.fill((168,30,20))
        self.id = id
        self.player = player
        
    def render(self, screen):
        print('am i rendering the spawn?')
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
        
        