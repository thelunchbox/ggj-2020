from rbt.game_components.bot import Bot


# This class represents the player

class Player:
    def __init__(self, ):
        self.connection = 0
        self.address = 0
        self.resource = 0
        self.bots = []

    # Create a bot and add it to the list of existing bots. Increment bot count by 1.
    def createBot(self):
        self.bots.add(Bot());




