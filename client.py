#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import functions
import basic


class Client(basic.Basic):
    TCP_PORT = 5011    #numer portu
    BUFFER_SIZE = 512
    socket = 0

    def __init__(self):
        for field in range(9):
            self.board.append(' ')

    def connect(self, ip):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, self.TCP_PORT))

    def receive_date(self):
        serialized_board = self.socket.recv(self.BUFFER_SIZE)
        self.board = functions.deserialization(serialized_board)
        self.print_board()
        return True

    def move(self):
        while 1:
            try:
                field = int(input("Second player's move. Choose a spot using numbers 0-8:   "))
                if not self.check_if_given_field_correct(field):
                    print("Try again")
                else:
                    self.board[field] = "X"
                    self.print_board()
                    break
            except ValueError:
                print("You can give only integer value.")
        serialized_board = functions.serialization(self.board)
        self.socket.send(serialized_board)

    def close_connection(self):
        self.socket.close()
