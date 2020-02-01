from rbt.game_components.bot import Bot

# This class represents the player
class Player():
    def __init__(self, ):
        self.connection = 0
        self.address = 0
        self.resource = 0
        self.botCount = 0

    # Create a bot and add it to the list of existing bots. Increment bot count by 1.
    def createBot(self, bots):
        bot = Bot();
        bots.add(bots);
        self.botCount+1;


    #TODO: Own and render a circle