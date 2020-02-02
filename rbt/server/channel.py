import json
from PodSixNet.Channel import Channel
from rbt.utils.utils import getId

class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        self.player = None
        self.game = None
        Channel.__init__(self, *args, **kwargs)

    def Network(self, data):
        pass

    def Close(self):
        self._server.RemovePlayer(self)

    def Network_updatePlayer(self, data):
        self.player.pos = data['data']["pos"] # simply update the coordinates of the player for now

    def Network_addBot(self, data):
        # create a new bot with a number of ports
        self.player.create_bot(getId(), data['data']['ports'])

    def Network_makeTool(self, data):
        self.player.make_tool(getId(), data['data']['tooltype'])

    def Network_deployBot(self, data):
        # get a bot from the player's inventory (or cheat in dev)

        #### DEV ONLY ####
        bot = self.player.create_bot(getId(), 2)
        # if we did not create a bot, we were out of resources
        if (not bot):
            return False
        #### DEV ONLY ####

        # and then add it to the tile at the coordinates specified
        pos = data['data']['pos']
        x = pos[0]
        y = pos[1]
        self.game.map.tiles[x][y].addEntity(bot)