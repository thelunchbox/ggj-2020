#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import json                 # import json module... duh

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))

msg = json.loads(s.recv(1024).decode('utf-8'))
while not msg.get('close', False):
    print("Name", msg["name"])
    print("Is he beautiful", msg["beautiful"])
    print("What kind of tail is his hair in?", msg["tail"])
    msg = json.loads(s.recv(1024).decode('utf-8'))

print('goodbye all my hard work')
s.close()                     # Close the socket when done