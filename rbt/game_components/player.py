from rbt.game_components.bot import Bot


# This class represents the player

class Player:
    def __init__(self, playerID):
        self.playerID = playerID
        self.connection = 0
        self.address = 0
        self.resource = 300
        self.bots = []

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







