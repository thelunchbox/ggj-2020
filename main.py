import sys
from rbt.client.client import Client
from rbt.utils.constants import PORT

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host")
        print("e.g.", sys.argv[0], "192.168.1.1")
    else:
        host = sys.argv[1]
        client = Client(host, PORT)
        client.run()
