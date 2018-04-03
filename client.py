#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import functions


class Client(object):
    TCP_IP = "127.0.0.1"    #host
    TCP_PORT = 5005     #numer portu
    BUFFER_SIZE = 1024
    board = []
    socket = 0

    def __init__(self):
        for field in range(9):
            self.board.append(' ')

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.TCP_IP, self.TCP_PORT))
        print("polaczono")

    def print_board(self):
        for field in range(9):
            if field%3 == 0:
                print("\n-----------")
            # print(" %c " % self.board[field], end = '')
            # if (field+1)%3 != 0:
                # print("|", end = '')
        # print("\n-----------")

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
                # server.Server.mock_board()
                return False
        else:
            print("Bad value, you have to use integer. Use a number from range 0-8 to make a move. For reference:")
            # server.Server.mock_board()
            return False

    def receive_date(self):
        serialized_board = self.socket.recv(self.BUFFER_SIZE)
        print("odebralem")
        if not serialized_board:
            print("odebrane zle dane")
        self.board = functions.deserialization(serialized_board)
        print("rozpakowalem")
        print(self.board)
        return True

    def move(self):
        print("zaczynam move")
        while 1:
            try:
                field = int(input("Second player's move. Choose a spot using numbers 0-8:   "))
                if not self.check_if_given_field_correct(field):
                    print("Try again")
                else:
                    self.board[field] = "X"
                    print("wybrano pole", self.board)
                    break
            except ValueError:
                print("You can give only integer value.")
        serialized_board = functions.serialization(self.board)
        self.socket.send(serialized_board)

    def close_connection(self):
        self.socket.close()
        print("zamknieto polaczenia")


new_client = Client()
new_client.connect()
while new_client.receive_date():
    new_client.move()

new_client.close_connection()

