import socket
from ..serialization import *


class Server(object):

    TCP_PORT = 5009  # numer portu
    connection = 0
    address = 0
    BUFFER_SIZE = 512
    socket = 0

    def connection(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind(('', self.TCP_PORT))
            print("Server is online. Waiting for a player to connect to you. (You have to give them your IP!)")
            self.socket.listen(1)
            self.connection, self.address = self.socket.accept()
        except OSError:
            print("Problems with connection.")
            return False
        return True

    def send_data(self, data):
        self.connection.send(serialize(data))

    def receive_data(self):
        data = deserialization(self.connection.recv(self.BUFFER_SIZE))
        if data.header == 'toPrint':
            print(data.msg)
        elif data.header == 'number':
            return data.msg
        else:
            print("Incorrect header")

    def close_connection(self):
        self.socket.close()
