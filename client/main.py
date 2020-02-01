import pygame
import time

pygame.init()
pygame.display.set_caption("REPAIR GAME")
screen = pygame.display.set_mode((1500,1020))
done = False

class Circle():
    def __init__(self):
        self.pos = (100,100)
        self.surface = pygame.Surface((30,30))
        self.surface.fill((255,100,100))
    def set_pos(self, pos):
        self.pos = pos
    def render(self, screen):
        screen.blit(self.surface, self.pos)


circleObject = Circle()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            done = True

        if pygame.mouse.get_pressed()[0]:
            coords = pygame.mouse.get_pos()
            circleObject.set_pos(coords)

    screen.fill((0,0,0))
    circleObject.render(screen)
    pygame.display.flip()


pygame.display.quit()
