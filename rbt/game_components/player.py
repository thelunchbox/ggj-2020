import pygame
import random
from rbt.game_components.bot import Bot

# This class represents the player
from rbt.game_components.test_entities import Circle
from rbt.utils.constants import PLAYER_COLORS, STARTING_RESOURCES


class Player(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 100))
        self.id = id
        self.connection = 0
        self.address = 0
        self.resource = STARTING_RESOURCES
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
            print(self.id, 'player out of resources!')

    def get_bot(self, botID):
        for bot in self.bots:
            if bot.id == botID:
                return bot

    def update(self):
        pass

    def getState(self):
        return {
            "id": self.id,
            "pos": self.pos,
            "resource": self.resource,
        }

    def captureInput(self, inputs):
        self.inputs = inputs

    def render(self, screen):
        self.circle.render(screen, self.pos)

    def setFromState(self, playerState):
        self.pos = playerState['pos']
        self.resource = playerState['resource']