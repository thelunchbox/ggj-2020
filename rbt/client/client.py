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

    def run(self):
        pygame.init()
        pygame.display.set_caption("REPAIR GAME")
        screen = pygame.display.set_mode((1500,1020))

        ## Wait to start until I get an initial game state
        ##################################################
        while len(self.game.players.values()) != 2:
            ## Get updates from the server
            ##############################
            print("Waiting for other players", len(self.game.players.values()), "found so far...")
            self.serverConnection.poll()

        done = False
        while not done:

            ## Get updates from the server
            ##############################
            # print("pump the server")
            self.serverConnection.poll()

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
                    self.serverConnection.send("updatePlayer", { "pos": coords })


            ## Render the screen
            ####################
            screen.fill((0,0,0))
            self.game.render(screen)
            pygame.display.flip()
        
        # when we're done...
        pygame.display.quit()

        print("Closing connection to server")