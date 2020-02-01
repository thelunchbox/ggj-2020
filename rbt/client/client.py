import pygame
import time
from rbt.game_components import test_entities

pygame.init()
pygame.display.set_caption("REPAIR GAME")
screen = pygame.display.set_mode((1500,1020))
done = False



circleObject = test_entities.Circle(1)

while not done:

    ## Get inputs
    #############

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            done = True

        if pygame.mouse.get_pressed()[0]:
            coords = pygame.mouse.get_pos()
            circleObject.set_pos(coords)


    ## Send inputs to the server
    ############################


    ## Get updates from the server
    ##############################


    ## Render the screen
    ####################
    screen.fill((0,0,0))
    circleObject.render(screen)
    pygame.display.flip()


pygame.display.quit()
