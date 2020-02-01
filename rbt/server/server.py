#!/usr/bin/python
import time
from rbt.server.server_channel import ServerChannel

def run(host, port):
    gameServer = ServerChannel(localaddr=(host, port))

    while True:
        gameServer.Pump()
        time.sleep(0.0016)
        gameServer.Process()