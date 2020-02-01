import pygame


class Circle():
    def __init__(self, playerID):
        self.player = playerID
        self.pos = (100,100)
        self.surface = pygame.Surface((30,30))
        self.surface.fill((255,100,100))
    def set_pos(self, pos):
        self.pos = pos
    def render(self, screen):
        screen.blit(self.surface, self.pos)

