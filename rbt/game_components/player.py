from rbt.game_components.bot import Bot
from rbt.game_components.test_entities import Circle #TODO: Testing -> Remove later

colorMap = {
    "1": (255,0,0),
    "2": (0,255,0)
}

# This class represents the player
class Player():
    def __init__(self, playerID):
        self.playerID = playerID
        self.connection = 0
        self.address = 0
        self.resource = 0
        self.botCount = 0

        # TESTING: REMOVE LATER
        self.circle = Circle(colorMap[playerID])
        self.pos = (100,100)

    # Create a bot and add it to the list of existing bots. Increment bot count by 1.
    def createBot(self, bots):
        bot = Bot();
        bots.add(bots);
        self.botCount+1;


     def render(self, screen):
        self.circle.render(screen. self.pos)

     def setPlayerFromState(self, gameState):
        self.pos = gameState["players"][playerID].pos