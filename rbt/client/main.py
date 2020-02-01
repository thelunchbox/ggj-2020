import pygame
import time
from rbt.game_components import test_entities
from rbt.game_components.bot import Bot

pygame.init()
pygame.display.set_caption("REPAIR GAME")
screen = pygame.display.set_mode((1500, 1020))
done = False

circleObject = test_entities.Circle(1)
botCounter = 1;
botlist = []

while not done:

    ## Get inputs
    #############

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            done = True

        if pygame.mouse.get_pressed()[0]:
            coords = pygame.mouse.get_pos()
            circleObject.set_pos(coords)

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_b]:
            coords = pygame.mouse.get_pos()
            print(coords)
            botlist.append(Bot(botCounter, coords ))
            botCounter+=1

    ## Send inputs to the server
    ############################

    ## Get updates from the server
    ##############################

    ## Render the screen
    ###################
    screen.fill((0, 0, 0))
    circleObject.render(screen)
    for bot in botlist:
        bot.render(screen)git
    pygame.display.flip()

pygame.display.quit()
