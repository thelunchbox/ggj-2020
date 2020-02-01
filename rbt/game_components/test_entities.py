import pygame


class Circle():
    def __init__(self, color):
        self.surface = pygame.Surface((30,30))
        self.surface.fill(color)

    def render(self, screen, pos):
        screen.blit(self.surface, pos)

