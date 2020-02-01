#!/usr/bin/python
import time
from server_channel import ServerChannel

gameServer = ServerChannel()

while True:
    gameServer.Pump()
    time.sleep(0.0001)
    gameServer.Process()