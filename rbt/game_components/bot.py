import pygame


# This class represents the robots that the player controls

class Bot():
    def __init__(self, bot_id, pos):
        self.bot_id = bot_id
        self.surface = pygame.Surface((30,30))
        self.surface.fill((255,100,100))
        self.pos = pos
        self.speed = 1
        self.ttl = 32000 #TODO: replace with config
        self.inventory = []

    def set_pos(self, pos):
        self.pos = pos

    def render(self, screen):
        screen.blit(self.surface, self.pos)
