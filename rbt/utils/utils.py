import socket

def getHostAddr():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)