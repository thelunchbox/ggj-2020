import pygame
import time
from PodSixNet.Connection import ConnectionListener
from PodSixNet.Connection import connection
from rbt.game_components.game_state import GameState
from rbt.game_components import player
from rbt.utils.utils import serialize
from rbt.utils.utils import deserialize

playerID = None
GAME_STATE = GameState()

class Client(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))
        print("client started")

    def Network_updateGameState(self, data):
        GAME_STATE.setGameFromState(deserialize(data)["data"]["gameState"])
        # print("Got game state from server", data)

    def Network_setID(self, data):
        playerID = deserialize(data)["data"]["id"]
        print("Got id from server", playerID)

    def Network_gameAborted(self, data):
        print("Game has been cancelled!")
        exit()

    def send(self, action, data):
        connection.Send(serialize({"action": action, "data": data}))

    def poll(self):
        connection.Pump()
        self.Pump()

    # Built ins
    ###########

    def Network_error(self, data):
        print('error:', data['error'])
        connection.Close()

    def Network_disconnected(self, data):
        print('Server disconnected')
        exit()

    def Network_connected(self, data):
        print("You are now connected to the server")


def run(host, port):
    ## Establish server connection
    ##############################
    serverConnection = Client(host, port)
    # connect to the server - optionally pass hostname and port like: ("mccormick.cx", 31425)

    pygame.init()
    pygame.display.set_caption("REPAIR GAME")
    screen = pygame.display.set_mode((1500,1020))

    ## Wait to start until I get an initial game state
    ##################################################
    while len(GAME_STATE.players.values()) != 2:
        ## Get updates from the server
        ##############################
        print("Waiting for other players", len(GAME_STATE.players.values()), "found so far...")
        serverConnection.poll()

    done = False
    ## GameLOOP!
    ############

    while not done:

        ## Get updates from the server
        ##############################
        # print("pump the server")
        serverConnection.poll()

        ## Get inputs
        #############

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
                done = True

            ## Send inputs to the server
            ############################
            if pygame.mouse.get_pressed()[0]:
                coords = pygame.mouse.get_pos()
                print("Sending player update to server")
                serverConnection.send("updatePlayer", { "pos": coords })


        ## Render the screen
        ####################
        screen.fill((0,0,0))
        GAME_STATE.render(screen)
        pygame.display.flip()


    pygame.display.quit()

    print("Closing connection to server")