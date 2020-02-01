from rbt.game_components.bot import Bot
from rbt.game_components.test_entities import Circle #TODO: Testing -> Remove later

#colorMap = {
#    "1": (255,0,0),
#    "2": (0,255,0)
#}

# This class represents the player
class Player():
    def __init__(self, id):
        self.id = id
        self.resource = 0
        self.botCount = 0
        self.position = {
            "x": 0,
            "y": 0
        }
        self.inputs = {}

        # TESTING: REMOVE LATER
        self.circle = Circle((255,0,0))
        self.pos = (100,100)

    # Create a bot and add it to the list of existing bots. Increment bot count by 1.
    def createBot(self, bots):
        bot = Bot();
        bots.add(bots);
        self.botCount+1;

    def getState(self):
        return {
            "id": str(self.id),
            "pos": self.position
        }
    
    def captureInput(self, inputs):
        self.inputs = inputs

    def render(self, screen):
        self.circle.render(screen, self.pos)

    def setPlayerFromState(self, gameState):
        self.pos = gameState["players"][id].pos