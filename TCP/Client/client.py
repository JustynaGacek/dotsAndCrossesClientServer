import socket
from ..serialization import *


class Client:
    TCP_PORT = 5005  # numer portu
    BUFFER_SIZE = 512
    socket = 0

    def connect(self, ip):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((ip, self.TCP_PORT))
        except OSError:
            print("Connection problems. Check ip then try again.")
            return False
        return True

    def send_data(self, data):
        self.socket.send(serialize(data))

    def receive_data(self):
        data = deserialization(self.socket.recv(self.BUFFER_SIZE))
        if data.header == 'toPrint':
            print(data.msg)
            return ''
        elif data.header == 'number':
            return data.msg
        else:
            print("Incorrect header")

    def close_connection(self):
        self.socket.close()
