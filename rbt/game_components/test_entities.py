import pygame
import os


class Circle():
    def __init__(self, color):
        self.surface = pygame.image.load(os.path.join('rbt', 'images', 'Redtooth_64.png'))

    def render(self, screen, pos):
        screen.blit(self.surface, pos)

