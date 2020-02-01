#!/usr/bin/python

import socket               # Import socket module
import json                 # import json module... duh
from rbt.game_components.game_state import GameState
from rbt.game_components.player import Player

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

x = {
    "name": "Justin",
    "beautiful": True,
    "tail": "pony"
}

game = GameState()
maxPlayers = 1

s.listen(5)                 # Now wait for client connection.
while len(game.players) < maxPlayers:
   c, addr = s.accept()     # Establish connection with client. This is synchronous and blocks the thread!
   print('Got connection from', addr)
   p = Player(c, addr, len(game.players) + 1)
   response = {
       "id": p.id
   }
   p.connection.send(json.dumps(response).encode('utf-8'))
   game.players.append(p)

# while not game.isOver():
    # for p in players:
        # p.captureInput(json.loads(c.recv(1024).decode('utf-8')))
    # dt = time since last update
    # game.update(dt)
    # state = game.getState()
    # stateBuffer = json.dumps(state).encode('utf-8')
    # for p in players:
        # p.sendUpdate(stateBuffer)

# when the game is over, I tell the players the game is over
# maybe we start a new game automatically after X seconds?

for p in game.players:
    p.connection.send('{ "close": true }'.encode('utf-8'))
    p.connection.close()                # Close the connection