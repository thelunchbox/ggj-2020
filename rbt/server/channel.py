import json
from PodSixNet.Channel import Channel

class ClientChannel(Channel):

    def Network(self, data):
        self.inputs = json.loads(data.decode('utf-8'))