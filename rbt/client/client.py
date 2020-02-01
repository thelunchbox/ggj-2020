import pygame
import time
from rbt.client.clientChannel import ClientChannel
from rbt.game_components.game_state import GameState
from rbt.game_components import player, test_entities
from rbt.game_components.player import Player
from rbt.utils.constants import MAX_PLAYERS

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
        while len(self.game.players.values()) != MAX_PLAYERS:
            self.serverConnection.poll()

    def gameLoop(self):
        done = False
        while not done:

            ## Get updates from the server
            ##############################
            # print("pump the server")
            self.serverConnection.poll()

            ### TODO: move to game state? #################
            ## sprite groups
            all_sprites = pygame.sprite.Group()
            player1_bot_sprites = pygame.sprite.Group()
            player2_bot_sprites = pygame.sprite.Group()
            player_sprites = pygame.sprite.Group()

            ## init players
            player1 = Player(1)
            player2 = Player(2)
            player_sprites.add(player1)
            player_sprites.add(player2)

            # TODO : Move to constants
            player1YCoord = 20
            player2YCoord = 800
            randomXCoord = random.randrange(50, 1450)

            circleObject = test_entities.Circle(1)
            botCounter = 1;

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
                keystate = pygame.key.get_pressed()

                if keystate[pygame.K_1]:
                    bot = player1.create_bot(botCounter, 1 )
                    if bot:
                        bot.set_color((255,255,255))
                        bot.set_pos((randomXCoord, player1YCoord))
                        player1_bot_sprites.add(bot)
                        print(player1.resource)
                        botCounter+=1
                    elif keystate[pygame.K_2]:
                        bot = player1.create_bot(botCounter, 2)
                        if bot:
                            print("2");
                            bot.set_color((0,255,255))
                            bot.set_pos((randomXCoord, player1YCoord))
                            player1_bot_sprites.add(bot)
                            print(player1.resource)
                            botCounter+=1
                    elif keystate[pygame.K_3]:
                        bot = player2.create_bot(botCounter, 1)
                        if bot:
                            print("3");
                            bot.set_color((255,0,255))
                            bot.set_pos((randomXCoord, player2YCoord))
                            player2_bot_sprites.add(bot)
                            print(player2.resource)
                            botCounter+=1
                    elif keystate[pygame.K_4]:
                        bot = player2.create_bot(botCounter, 2)
                        if bot:
                            print("4");
                            bot.set_color((0,125,255))
                            bot.set_pos((randomXCoord, player2YCoord))
                            player2_bot_sprites.add(bot)
                            print(player2.resource)
                            botCounter+=1

            ## check collisions
            hits = pygame.sprite.groupcollide(player1_bot_sprites, player2_bot_sprites, True, True)

            ## update the sprites
            all_sprites.add(player_sprites)
            all_sprites.add(player1_bot_sprites)
            all_sprites.add(player2_bot_sprites)
            all_sprites.update()

            ## Render the screen
            ####################
            self.screen.fill((0,0,0))
            all_sprites.draw(self.screen)
            self.game.render(self.screen)
            pygame.display.flip()


    def cleanup(self):
        pygame.display.quit()
        print("Closing connection to server")

    def run(self):
        self.waitForPlayers()
        self.gameLoop()
        self.cleanup()
