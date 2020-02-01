from PodSixNet.Server import Server
from rbt.server.channel import ClientChannel
from rbt.game_components.game_state import GameState
from rbt.game_components.player import Player
from rbt.utils.utils import serialize

class ServerChannel(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        print("Starting server...")
        Server.__init__(self, *args, **kwargs)
        self.game = GameState()
        self.maxPlayers = 2
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
            channel.Send(serialize(response))
            self.game.players[p.id] = p
            channel.player = p
            self.connections[p.id] = channel
    
    def RemovePlayer(self, connection):
        del self.connections[connection.player.id]
        for c in self.connections.values():
            print('sending abort message to player', c.player.id)
            c.Send(serialize({ 
                "action": "gameAborted"
            }))
        print('Ending game because someone wussed out')
        exit()

    def Process(self):
        self.game.update()
        state = self.game.getState()
        if (len(state["players"].keys()) == self.maxPlayers):
            for c in self.connections.values():
                # print('sending game state to player', c.player.id, state)
                c.Send(serialize({ 
                    "action": "updateGameState",
                    "data": { "gameState" : state }
                }))
        else:
            pass
            #print('ignoring unready game state')
