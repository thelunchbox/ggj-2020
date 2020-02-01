#!/usr/bin/python

import socket               # Import socket module
import json                 # import json module... duh

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

x = {
    "name": "Justin",
    "beautiful": True,
    "tail": "pony"
}

players = []
maxPlayers = 1

s.listen(5)                 # Now wait for client connection.
while len(players) < maxPlayers:
   c, addr = s.accept()     # Establish connection with client. This is synchronous and blocks the thread!
   print('Got connection from', addr)
   c.send(json.dumps(x).encode('utf-8'))
   players.append(c)    # this will eventually be a new Player object

# create a new Game object
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

for c in players:
    c.send('{ "close": true }'.encode('utf-8'))
    c.close()                # Close the connection