#!/usr/bin/python
import time
from datetime import datetime
from rbt.server.server_channel import ServerChannel
from rbt.utils.constants import TICK_RATE
from rbt.utils.utils import ticks

def run(host, port):
    gameServer = ServerChannel(localaddr=(host, port))
    lastUpdate = 0

    while True:
        gameServer.Pump()
        time.sleep(0.001)
        gameServer.Process()
        # now = ticks(datetime.now())
        # if (now - lastUpdate >= TICK_RATE):
        #     gameServer.Process()
        #     lastUpdate = now