#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import functions


class Client(object):
    TCP_PORT = 5005     #numer portu
    BUFFER_SIZE = 512
    board = []
    socket = 0

    def __init__(self):
        for field in range(9):
            self.board.append(' ')

    def connect(self, ip):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, self.TCP_PORT))

    def print_board(self):
        for field in range(9):
            if field%3 == 0:
                print("\n-----------")
            print(" %c " % self.board[field], end = '')
            if (field+1)%3 != 0:
                print("|", end = '')
        print("\n-----------")

    @staticmethod
    def mock_board():
        print("How to play:\n", "Choose where do you want to play your dot or cross,\n",
              "by typing a number corresponding to the field below")
        for field in range(9):
            if field % 3 == 0:
                print("\n-----------")
            print(" " + str(field) + " ", end='')
            if (field + 1) % 3 != 0:
                print("|", end='')
        print("\n-----------")

    def check_if_given_field_correct(self, field):
        if isinstance(field, int):
            int(field)
            if 0 <= field <= 8:
                if self.board[field] == ' ':
                    print("Your choice was saved.")
                    return True
                else:
                    print("This field is already occupied. Please choose another free value.")
                    return False
            else:
                print("Bad number, use a number from range 0-8 to make a move. For reference:")
                self.mock_board()
                return False
        else:
            print("Bad value, you have to use integer. Use a number from range 0-8 to make a move. For reference:")
            self.mock_board()
            return False

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
