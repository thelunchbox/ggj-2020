import pygame
import random
from rbt.game_components.bot import Bot

# This class represents the player
from rbt.game_components.button import Button
from rbt.game_components.test_entities import Circle
from rbt.game_components.tools import Tool
from rbt.utils.constants import PLAYER_COLORS, STARTING_RESOURCES, TOOL_COST


class Player(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 100))
        self.id = id
        self.connection = 0
        self.address = 0
        self.resource = STARTING_RESOURCES
        self.tools = []
        tool = Tool(12,'attack',self.id)
        self.tools.append(tool)
        self.bots = []
        self.inputs = {}
        self.buttons = self.generate()
        self.yStart = 20 if id == 1 else 800

        # TESTING: REMOVE LATER
        self.circle = Circle(PLAYER_COLORS[self.id])
        self.pos = (100,100)

    # Create a bot and add it to the list of existing bots.
    def create_bot(self, botID, slots):
        resourceCost = 2 + (slots * 3)
        if resourceCost <= self.resource:
            bot = Bot(botID, slots, self.id)
            self.bots.append(bot)
            self.resource -= resourceCost
            # bot.set_pos((random.randrange(50, 1450), self.yStart)) # not yet...
            return bot
        else:
            print(self.id, 'player out of resources!', resourceCost, '>', self.resource)

    def get_bot(self, botID):
        for bot in self.bots:
            if bot.id == botID:
                return bot

    def update(self):
        pass

    def getState(self):
        botStates = {}
        toolStates = {}

        for bot in self.bots:
            botStates[bot.id] = bot.getState()
        for tool in self.tools:
            toolStates[tool.id] = tool.getState()
            
        return {
            "id": self.id,
            "pos": self.pos,
            "resource": self.resource,
            "bots": botStates,
            "tools": toolStates
        }

    def captureInput(self, inputs):
        self.inputs = inputs

    def render(self, screen):
        self.generate()
        for button in self.buttons:
            button.draw(screen)

    def generate(self):
        buttons= []
        resource_button = Button((255, 255, 255), 1100, 500, 200, 50, str(self.resource))
        buttons.append(resource_button)
        offset = 50
        for tool in self.tools:
            if isinstance(tool,Tool):
                tool_button = Button((255, 255, 255), 1100, 500 + offset, 200, 50, str(tool.type))
                buttons.append(tool_button)
                offset += 50
        return buttons

    def setFromState(self, playerState):
        self.pos = playerState['pos']
        self.resource = playerState['resource']
        self.bots = playerState['bots']
        self.tools = playerState['tools']

    def make_tool(self, toolID, type):
        print("making a tool", type, self.resource);
        if self.resource >= TOOL_COST:
            tool = Tool(toolID, type, self.id)
            self.tools.append(tool)
            self.resource-=TOOL_COST
            print("made tool", type, self.resource);
            return tool
        else:
            print(self.id, 'player out of resources!')

