import pygame
import time
from rbt.client.clientChannel import ClientChannel
from rbt.game_components.game_state import GameState
from rbt.game_components import player

class Client():
    def __init__(self, host, port):
        self.playerID = None
        self.game = GameState()
        self.serverConnection = ClientChannel(host, port, self)
        pygame.init()
        pygame.display.set_caption("REPAIR GAME")
        self.screen = pygame.display.set_mode((1500,1020))

    def waitForPlayers(self):
        print("Waiting for other players")
        while len(self.game.players.values()) != 2:
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
                    coords = pygame.mouse.get_pos()
                    self.serverConnection.send("updatePlayer", { "pos": coords })


            ## Render the screen
            ####################
            self.screen.fill((0,0,0))
            self.game.render(self.screen)
            pygame.display.flip()


    def cleanup(self):
        pygame.display.quit()
        print("Closing connection to server")

    def run(self):
        self.waitForPlayers()
        self.gameLoop()
        self.cleanup()
