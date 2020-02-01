import pygame

from rbt.game_components.bot import Bot

# This class represents the player

class Player(pygame.sprite.Sprite):
    def __init__(self, playerID):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 100))
        self.rect = self.image.get_rect()
        self.playerID = playerID
        self.connection = 0
        self.address = 0
        self.resource = 500
        self.bots = []
        self.inputs = {}

    # Create a bot and add it to the list of existing bots. Increment bot count by 1.
    def create_bot(self, botID, slots):
        resourceCost = 2 +  ( slots * 3 )
        if resourceCost <= self.resource:
            bot = Bot(botID, slots, self.playerID)
            self.bots.append(bot)
            self.resource-=resourceCost
            return bot

    def get_bot(self, botID):
        for bot in self.bots:
            if bot.botID == botID:
                return bot

    def update(self):
        self.draw()

    def draw_resource(self):
        # define the RGB value for white,
        #  green, blue colour .
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render( str("hi"), False, (0, 0, 0))

    def draw(self):
        self.draw_resource()

    def getState(self):
        return {
            "id": self.id,
            "pos": self.pos
        }

    def captureInput(self, inputs):
        self.inputs = inputs

    def setPlayerFromState(self, playerState):
        self.pos = playerState['pos']