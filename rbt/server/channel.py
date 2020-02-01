import json
from PodSixNet.Channel import Channel

class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        self.player = None
        Channel.__init__(self, *args, **kwargs)

    def Network(self, data):
        pass

    def Close(self):
        self._server.RemovePlayer(self)

    def Network_updatePlayer(self, data):
        self.player.pos = data['data']["pos"] # simply update the coordinates of the player for now