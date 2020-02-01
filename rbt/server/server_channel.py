import json

from PodSixNet.Server import Server
from channel import ClientChannel
from rbt.game_components.game_state import GameState
from rbt.game_components.player import Player

class ServerChannel(Server):
    
    channelClass = ClientChannel
    game = GameState()
    maxPlayers = 1
    
    def Connected(self, channel, addr):
        if len(self.game.players) < self.maxPlayers:
            p = Player(channel, addr, len(self.game.players) + 1)
            response = {
                "id": p.id
            }
            p.connection.send(json.dumps(response).encode('utf-8'))
            self.game.players.append(p)

    def Process(self):
        for p in self.game.players:
            p.captureInput(p.connection)
        self.game.update()
        state = self.game.getState()
        stateBuffer = json.dumps(state).encode('utf-8')
        for p in self.game.players:
            p.sendUpdate(stateBuffer)
