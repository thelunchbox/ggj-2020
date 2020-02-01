import pygame
import random


# This class represents the robots that the player controls

class Bot(pygame.sprite.Sprite):

    def __init__(self, botID, slots, owner):
        pygame.sprite.Sprite.__init__(self)
        self.botID = botID
        self.image = pygame.Surface((30,30))
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = 50
        self.slots = slots
        self.speed = 2
        self.direction = (0,0)
        self.ttl = 32000 #TODO: replace with config
        self.inventory = []
        self.owner = owner

    def set_pos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_color(self, color):
        self.image.fill(color)

    def update(self):
        # self.direction = random.choice(((1,0), (0, 1), (-1, 0), (0, -1)))
        if self.owner == 1:
            self.rect.y+=self.speed
        else:
            self.rect.y-= self.speed




