#!/usr/bin/python

import socket               # Import socket module
import json                 # import json module... duh

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

x = {
    "name": "Justin",
    "beautiful": "yes",
    "tail": "pony"
}

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client. This is synchronous and blocks the thread!
   print('Got connection from', addr)
   c.send(json.dumps(x).encode('utf-8'))
   c.close()                # Close the connection
   exit()