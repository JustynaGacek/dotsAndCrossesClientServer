#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..Shared import basic
from TCP.serialization import *


class Client(basic.Basic):

    TCP_PORT = 5009    #numer portu
    BUFFER_SIZE = 512
    socket = 0

    def __init__(self, socket):
        for field in range(9):
            self.board.append(' ')
        self.socket = socket

    def receive_data(self):
        serialized_board = self.socket.recieve_data(self.BUFFER_SIZE)
        self.board = deserialization(serialized_board)
        for field in range(9):
            if field%3 == 0:
                print("\n-----------")
            print(" %c " % self.board[field], end = '')
            if (field+1)%3 != 0:
                print("|", end = '')
        print("\n-----------")
        if self.board.msg == "You lost." or self.board.msg == "You won!":
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
        serialized_field = serialize(field)
        self.socket.send(serialized_field)

