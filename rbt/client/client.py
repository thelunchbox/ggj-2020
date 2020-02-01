import pygame
import time
from PodSixNet.Connection import ConnectionListener
from PodSixNet.Connection import connection
from rbt.game_components import test_entities
from rbt.game_components import player

pygame.init()
pygame.display.set_caption("REPAIR GAME")
screen = pygame.display.set_mode((1500,1020))
done = False
playerID = None
GAME_STATE = None

class ClientListener(ConnectionListener):
    def Network_updateGameState(data):
       GAME_STATE = data["gamestate"]
       print("Got game state from server", GAME_STATE)

    def Network_setID(data):
        playerID = data["data"]["id"]
        print("Got id from server", playerID)


#circleObject = test_entities.Circle(1) #TODO: Use a game state object here instead


## Establish server connection
##############################
# connect to the server - optionally pass hostname and port like: ("mccormick.cx", 31425)
connection.Connect()


## Wait to start until I get an initial game state
##################################################
while not GAME_STATE:
    ## Get updates from the server
    ##############################
    ClientListener.pump()


## GameLOOP!
############

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
            #circleObject.set_pos(coords) #TODO: Send click to server instead (command, pos) { "command": "click", "data": {"x": 11, "y": 11} }
            print("Sending player update to server")
            connection.Send({"action": "updatePlayer", "data": { "pos": coords}})


    ## Get updates from the server
    ##############################
    print("pump the server")
    ClientListener.pump()



    ## Render the screen
    ####################
    screen.fill((0,0,0))
    #circleObject.render(screen)
    pygame.display.flip()


pygame.display.quit()

print("Closing connection to server)"
gameServer.close()