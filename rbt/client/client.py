import pygame, objgraph
import time
from rbt.client.clientChannel import ClientChannel
from rbt.game_components.game_state import GameState
from rbt.game_components import player
from rbt.utils.constants import MAX_PLAYERS, SCREEN_RESOLUTION
from rbt.utils.utils import mapCoords


class Client():
    def __init__(self, host, port):
        self.playerID = None
        self.game = GameState()
        self.serverConnection = ClientChannel(host, port, self)
        pygame.init()
        pygame.display.set_caption('GREMLIN DONGLES')
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION)

    def waitForPlayers(self):
        print("Waiting for other players")
        while len(self.game.players.values()) != MAX_PLAYERS:
            self.serverConnection.poll()

    def gameLoop(self):
        done = False
        while not done:

            ## Get updates from the server
            ##############################
            # print("pump the server")
            self.serverConnection.poll()

            ## Get Events
            #############
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
                    done = True

                ## Send inputs to the server
                ############################
                if pygame.mouse.get_pressed()[0]:
                    coords = mapCoords(pygame.mouse.get_pos())
                    if (coords[0] < 16 and coords[1] < 16 and coords[0] >= 0 and coords[1] >= 0):
                        # this is a click on the MAP
                        if (self.game.map.isSpawn(coords, self.playerID)):
                            self.serverConnection.send("deployBot", { "pos": coords })
                    else:
                        pass # here we process clicks on the UI elements
                    
                keystate = pygame.key.get_pressed()

                if keystate[pygame.K_1]:
                    self.serverConnection.send("addBot", { 'ports': 1 })
                elif keystate[pygame.K_2]:
                    self.serverConnection.send("addBot", { 'ports': 2 })
                elif keystate[pygame.K_3]:
                    self.serverConnection.send("addBot", { 'ports': 3 })
                elif keystate[pygame.K_4]:
                    self.serverConnection.send("addBot", { 'ports': 4 })
                elif keystate[pygame.K_5]:
                    self.serverConnection.send("makeTool", {'toolType': 'attack'})
                elif keystate[pygame.K_6]:
                    self.serverConnection.send("makeTool", {'toolType': 'gather'})
                elif keystate[pygame.K_7]:
                    self.serverConnection.send("makeTool", {'toolType': 'build'})
                elif keystate[pygame.K_8]:
                    self.serverConnection.send("makeTool", {'toolType': 'signal'})
                elif keystate[pygame.K_9]:
                    print("==============")
                    objgraph.show_most_common_types(50)
                    print("")


            ## Render the screen
            ####################
            self.game.render(self.screen)
            pygame.display.flip()


    def cleanup(self):
        pygame.display.quit()
        print("Closing connection to server")

    def run(self):
        self.waitForPlayers()
        self.gameLoop()
        self.cleanup()
