from PodSixNet.Connection import ConnectionListener
from PodSixNet.Connection import connection
from rbt.game_components.game_state import GameState
from rbt.game_components import player

class ClientChannel(ConnectionListener):
    def __init__(self, host, port, client):
        self.Connect((host, port))
        self.client = client
        print("client started")

    def Network_updateGameState(self, data):
        self.client.game.setGameFromState(data["data"]["gameState"])
        # print("Got game state from server", data)

    def Network_setID(self, data):
        self.client.playerID = data["data"]["id"]
        print("Got id from server", self.client.playerID)

    def Network_gameAborted(self, data):
        print("Game has been cancelled!")
        exit()

    def send(self, action, data):
        connection.Send({"action": action, "data": data})

    def poll(self):
        connection.Pump()
        self.Pump()

    # Built ins
    ###########

    def Network_error(self, data):
        print('error:', data['error'])
        connection.Close()

    def Network_disconnected(self, data):
        print('Server disconnected')
        exit()

    def Network_connected(self, data):
        print("You are now connected to the server")