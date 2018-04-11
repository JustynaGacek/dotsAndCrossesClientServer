#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from ..Shared import basic
from ..Shared import functions


class Client(basic.Basic):

    TCP_PORT = 5009    #numer portu
    BUFFER_SIZE = 512
    socket = 0

    def __init__(self):
        for field in range(9):
            self.board.append(' ')

    def connect(self, ip):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((ip, self.TCP_PORT))
        except OSError:
            print("Connection problems. Check ip then try again.")
            return False
        return True

    def receive_data(self):
        serialized_board = self.socket.recv(self.BUFFER_SIZE)
        self.board = functions.deserialization(serialized_board)
        if self.board == "You lost." or self.board == "You won!":
            self.print_board()
            print(self.board, "Thanks for playing!")
            self.close_connection()
            return False
        self.print_board()
        return True

    def move(self):
        while 1:
            try:
                field = int(input("Your turn. Choose a spot using numbers 0-8:   "))
                if not self.check_if_given_field_correct(field):
                    print("Incorrect input. Only integers form 0 to 8 are valid.")
                else:
                    self.board[field] = "X"
                    self.print_board()
                    break
            except ValueError:
                print("You can only input integer value ranging from 0 to 8.")
                self.mock_board()
        serialized_field = functions.serialization(field)
        self.socket.send(serialized_field)

    def close_connection(self):
        self.socket.close()
