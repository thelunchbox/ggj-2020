import pygame
import random
from rbt.game_components.bot import Bot

# This class represents the player
from rbt.game_components.test_entities import Circle
from rbt.utils.constants import PLAYER_COLORS


class Player(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 100))
        self.id = id
        self.connection = 0
        self.address = 0
        self.resource = 500
        self.bots = []
        self.inputs = {}

        self.yStart = 20 if id == 1 else 800

        # TESTING: REMOVE LATER
        self.circle = Circle(PLAYER_COLORS[self.id])
        self.pos = (100,100)

    # Create a bot and add it to the list of existing bots.
    def create_bot(self, botID, slots):
        resourceCost = 2 + ( slots * 3 )
        if resourceCost <= self.resource:
            bot = Bot(botID, slots, self.id)
            self.bots.append(bot)
            self.resource -= resourceCost
            bot.set_pos((random.randrange(50, 1450), self.yStart))
            return bot
        else:
            print('out of resources!')

    def get_bot(self, botID):
        for bot in self.bots:
            if bot.botID == botID:
                return bot

    def update(self):
        for bot in self.bots:
            bot.update()

    def getState(self):
        botStates = {}
        for bot in self.bots:
            botStates[bot.botID] = bot.getState()

        return {
            "id": self.id,
            "pos": self.pos,
            "resource": self.resource,
            "bots": botStates
        }

    def captureInput(self, inputs):
        self.inputs = inputs

    def render(self, screen):
        self.circle.render(screen, self.pos)
        for bot in self.bots:
            bot.render(screen)


    def setPlayerFromState(self, playerState):
        # create any new player that doesn't exist
        for botID in playerState['bots'].keys():
            if (not self.get_bot(botID)):
                bot = Bot(botID, playerState['bots'][botID]['slots'], self.id)
                bot.set_color((0,255,0))
                self.bots.append(bot)
                print('how many bots do you wish', len(self.bots))

        for bot in self.bots:
            bot.setBotFromState(playerState['bots'][bot.botID])

        self.pos = playerState['pos']
        self.resource = playerState['resource']