import socket


class ipAddress:

    def __init__(self):
        self.hostname = socket.gethostname()

    def getIpAddres(self):
        return socket.gethostbyname(self.hostname)



