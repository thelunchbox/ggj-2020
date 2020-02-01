import pygame
import random
from rbt.game_components import test_entities
from rbt.game_components.player import Player

pygame.init()
pygame.display.set_caption("REPAIR GAME")
screen = pygame.display.set_mode((1500, 1020))
done = False

## sprite groups
circleObject = test_entities.Circle(1)
all_sprites = pygame.sprite.Group()
bot_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()

## init players
player1 = Player(1)
player2 = Player(2)
player_sprites.add(player1)
player_sprites.add(player2)

botCounter = 1;

while not done:

    ## Get inputs
    #############

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            done = True

        player1YCoord = 20
        player2YCoord = 800
        randomXCoord = random.randrange(50, 1450)
        coords = pygame.mouse.get_pos()
        keystate = pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0]:
            circleObject.set_pos(coords)
            print(coords)
        if keystate[pygame.K_1]:
            bot = player1.create_bot(botCounter, 1 )
            if bot:
                bot.set_color((255,255,255))
                bot.set_pos((randomXCoord, player1YCoord))
                bot_sprites.add(bot)
                print(player1.resource)
                botCounter+=1
        elif keystate[pygame.K_2]:
            bot = player1.create_bot(botCounter, 2 )
            if bot:
                bot.set_color((0,255,255))
                bot.set_pos((randomXCoord, player1YCoord))
                bot_sprites.add(bot)
                print( player1.resource )
                botCounter+=1
        elif keystate[pygame.K_3]:
            bot = player2.create_bot(botCounter, 1 )
            if bot:
                bot.set_color((255,0,255))
                bot.set_pos((randomXCoord, player2YCoord))
                bot_sprites.add(bot)
                print( player2.resource )
                botCounter+=1
        elif keystate[pygame.K_4]:
            bot = player2.create_bot(botCounter, 2 )
            if bot:
                bot.set_color((0,125,255))
                bot.set_pos((randomXCoord, player2YCoord))
                bot_sprites.add(bot)
                print( player2.resource )
                botCounter+=1

    ## Send inputs to the server
    ############################

    ## Get updates from the server
    ##############################

    ## update the sprites
    all_sprites.add(player_sprites)
    all_sprites.add(bot_sprites)
    all_sprites.update()


    ## Render the screen
    ###################
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.display.quit()
