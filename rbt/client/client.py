import pygame
#import objgraph
import time
from rbt.client.clientChannel import ClientChannel
from rbt.game_components.hud import Button
from rbt.game_components.game_state import GameState
from rbt.game_components import player
from rbt.utils.constants import MAX_PLAYERS, SCREEN_RESOLUTION, ATTACK_BUTTON_X, ATTACK_BUTTON_Y, GATHER_BUTTON_X, \
    BUILD_BUTTON_X, SIGNAL_BUTTON_X, SIGNAL_BUTTON_Y, BUILD_BUTTON_Y, GATHER_BUTTON_Y
from rbt.utils.utils import mapCoords, isOver


class Client():
    def __init__(self, host, port):
        self.playerID = None
        self.game = GameState()
        self.serverConnection = ClientChannel(host, port, self)
        pygame.init()
        pygame.display.set_caption('BLUETOOTH BYTES')
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION, pygame.FULLSCREEN)
        pygame.mixer.music.load('BTB_Overture.wav')
        pygame.mixer.music.play(-1)

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
                    screenCoords = pygame.mouse.get_pos()
                    if (coords[0] < 16 and coords[1] < 16 and coords[0] >= 0 and coords[1] >= 0):
                        # this is a click on the MAP
                        if (self.game.map.isSpawn(coords, self.playerID)):
                            self.serverConnection.send("deployBot", { "pos": coords })
                    else:
                        if(isOver((ATTACK_BUTTON_X, ATTACK_BUTTON_Y ), screenCoords) ):
                            self.serverConnection.send("makeTool", {'type': 'attack'})
                        if(isOver((GATHER_BUTTON_X, GATHER_BUTTON_Y ), screenCoords) ):
                            self.serverConnection.send("makeTool", {'type': 'gather'})
                        if(isOver((BUILD_BUTTON_X, BUILD_BUTTON_Y ), screenCoords) ):
                            self.serverConnection.send("makeTool", {'type': 'build'})
                        if(isOver((SIGNAL_BUTTON_X, SIGNAL_BUTTON_Y ), screenCoords) ):
                            self.serverConnection.send("makeTool", {'type': 'signal'})
                    
                keystate = pygame.key.get_pressed()

                if keystate[pygame.K_1]:
                    self.serverConnection.send("addBot", { 'ports': 1 })
                elif keystate[pygame.K_2]:
                    self.serverConnection.send("addBot", { 'ports': 2 })
                elif keystate[pygame.K_3]:
                    self.serverConnection.send("addBot", { 'ports': 3 })
                elif keystate[pygame.K_4]:
                    self.serverConnection.send("addBot", { 'ports': 4 })

                #elif keystate[pygame.K_9]:
                #    print("==============")
                #    objgraph.show_most_common_types(50)
                #    print("")


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
