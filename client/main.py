import pygame
import time

pygame.init()
pygame.display.set_caption("REPAIR GAME")
screen = pygame.display.set_mode((1500,1020))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            done = True

    screen.fill((0,0,0))
    pygame.display.flip()


pygame.display.quit()
