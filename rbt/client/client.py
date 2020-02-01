import pygame
import time
import socket
import json
from rbt.game_components import test_entities
from rbt.game_components import player

pygame.init()
pygame.display.set_caption("REPAIR GAME")
screen = pygame.display.set_mode((1500,1020))
done = False



## Establish server connection
##############################
gameServer = socket.socket()         # Create a socket object
host = socket.gethostname()                # Get local machine name
port = 12345                               # Reserve a port for your service.
gameServer.connect((host, port))

## Get my player ID from the server
###################################
message = json.loads(gameServer.recv(1024).decode('utf-8'))

myPlayer = player.Player(msg["playerID"])

## Wait to start until I get an initial game state
##################################################
serverState = json.loads(gameServer.recv(1024).decode('utf-8'))

circleObject = test_entities.Circle(1) #TODO: Use a game state object here instead

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
    circleObject.render(screen)
    pygame.display.flip()


pygame.display.quit()

gameServer.close()