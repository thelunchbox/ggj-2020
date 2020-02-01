from PodSixNet.Server import Server
from rbt.server.channel import ClientChannel
from rbt.game_components.game_state import GameState
from rbt.game_components.player import Player

class ServerChannel(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        print("Starting server...")
        Server.__init__(self, *args, **kwargs)
        self.game = GameState()
        self.maxPlayers = 1
        self.connections = {}

    def Connected(self, channel, addr):
        print("Client connecting..")
        if len(self.game.players.keys()) < self.maxPlayers:
            p = Player(len(self.game.players.keys()) + 1)
            response = {
                "action": "setId",
                "data": { "id": p.id }
            }
            print('sending id to player', p.id, response)
            channel.send(response)
            self.game.players[str(p.id)] = p
            channel.player = p
            self.connections[str(p.id)] = channel

    def Process(self):
        self.game.update()
        state = self.game.getState()
        if (len(state["players"].keys()) == self.maxPlayers):
            for c in self.connections.values():
                print('sending game state to player', c.player.id, state)
                c.send({ 
                    "action": "updateGameState",
                    "data": { "gameState" : state }
                })
        else:
            pass
            #print('ignoring unready game state')
