<<<<<<< HEAD


import rbt.server.server
=======
import sys
from rbt.server.server import run
from rbt.utils.constants import PORT
from rbt.utils.utils import getHostAddr

if __name__ == '__main__':
    host = getHostAddr()
    print('Running server at', host)
    run(host, PORT)
>>>>>>> master
