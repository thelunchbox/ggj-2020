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

class Client(ConnectionListener):
    def __init__(self):
       self.Connect()
       print("client started")

    def Network_updateGameState(self, data):
       GAME_STATE = data["gamestate"]
       print("Got game state from server", GAME_STATE)

    def Network_setID(self, data):
        playerID = data["data"]["id"]
        print("Got id from server", playerID)

    def send(self, action, data):
        connection.Send({"action": action, "data": data})

    # Built ins
    ###########

    def loop(self):
        connection.Pump()
        self.Pump()

    def Network_error(self, data):
        print('error:', data['error'])
        connection.Close()

    def Network_disconnected(self, data):
        print('Server disconnected')
        exit()

    def Network_connected(self, data):
        print("You are now connected to the server")


#circleObject = test_entities.Circle(1) #TODO: Use a game state object here instead


## Establish server connection
##############################
serverConnection = Client()
# connect to the server - optionally pass hostname and port like: ("mccormick.cx", 31425)


## Wait to start until I get an initial game state
##################################################
while not GAME_STATE:
    ## Get updates from the server
    ##############################
    serverConnection.loop()


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
            connection.Send("updatePlayer", { "pos": coords })


    ## Get updates from the server
    ##############################
    print("pump the server")
    serverConnection.loop()



    ## Render the screen
    ####################
    screen.fill((0,0,0))
    #circleObject.render(screen)
    pygame.display.flip()


pygame.display.quit()

print("Closing connection to server")