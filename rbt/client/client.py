import pygame
import time
from rbt.game_components import test_entities
from rbt.game_components import map

pygame.init()
pygame.display.set_caption("REPAIR GAME")
screen = pygame.display.set_mode((1500,1020))
done = False



#TODO: establish server connection

#TODO: Get my player ID from the server

#TODO: wait to start until I get an initial game state

circleObject = test_entities.Circle(1) #TODO: Use a game state object here instead
m = map.Map()

while not done:

    ## Get inputs
    #############

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            done = True



    ## Send inputs to the server
    ############################
        if pygame.mouse.get_pressed()[0]:
            coords = pygame.mouse.get_pos()
            circleObject.set_pos(coords) #TODO: Send click to server instead (command, pos) { "command": "click", "data": {"x": 11, "y": 11} }


    ## Get updates from the server
    ##############################

    #TODO: Get game state from server and update my game state


    ## Render the screen
    ####################
    screen.fill((0,0,0))
    m.render(screen)
    circleObject.render(screen)
    pygame.display.flip()


pygame.display.quit()
