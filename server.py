# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import socket
import functions


class Server(object):
    """ class representing the game of a dots and crosses """

    board = []
    rows = [0, 0, 0]
    columns = [0, 0, 0]
    diagonals = [0, 0]
    winning_flag = 0

    TCP_IP = "127.0.0.1"  # host
    TCP_PORT = 5005  # numer portu
    BUFFER_SIZE = 1024
    socket = 0
    connection = 0
    address = 0

    def __init__(self):
        for field in range(9):
            self.board.append(' ')

    def connection(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.TCP_IP, self.TCP_PORT))
        self.socket.listen(1)
        self.connection, self.address = self.socket.accept()
        print("polaczono")

    def winning_condition_increment(self, field, increment_value):
        """method used to assert how close players are to winning"""
        self.rows[math.floor(field / 3)] += increment_value
        self.columns[field % 3] += increment_value
        if field in {0, 4, 8}:
            self.diagonals[0] += increment_value
        if field in {2, 4, 6}:
            self.diagonals[1] += increment_value

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
                Server.mock_board()
                return False
        else:
            print("Bad value, you have to use integer. Use a number from range 0-8 to make a move. For reference:")
            Server.mock_board()
            return False

    def first_user_move(self):
        try:
            field = int(input("First player's move. Choose a spot using numbers 0-8:   "))
            if self.check_if_given_field_correct(field):
                self.board[field] = "O"
                # self.winning_condition_increment(field, -1)
                return True
            else:
                return False
        except ValueError:
            print("You can give only integer value.")

    def second_user_move_send_board(self):
        serialized_board = functions.serialization(self.board)
        print("serwer serializuje tablice")
        self.connection.send(serialized_board)
        print("serwer wysyla tablice")
        return True

    def second_user_move_receive_board(self):
        # while 1:
        serialized_board = self.connection.recv(self.BUFFER_SIZE)
            # if not serialized_board: break
        print("otrzymalem dane")
        self.board = functions.deserialization(serialized_board)
        print(self.board)
        return True
        # self.winning_condition_increment(field, -1)     #help ??

    @staticmethod
    def print_board(self):
        for field in range(9):
            if field % 3 == 0:
                print("\n-----------")
        #     print(" %c " % self.board[field], end='')
        #     if (field + 1) % 3 != 0:
        #         print("|", end='')
        # print("\n-----------")

    @staticmethod
    def mock_board():
        print("How to play:\n", "Choose where do you want to play your dot or cross,\n",
              "by typing a number corresponding to the field below")
        for field in range(9):
            if field % 3 == 0:
                print("\n-----------")
        #     print(" " + str(field) + " ", end='')
        #     if (field + 1) % 3 != 0:
        #         print("|", end='')
        # print("\n-----------")

    def winning_condition_check(self):
        """method that checks winning conditions for both players"""
        if -3 in self.rows or -3 in self.columns or -3 in self.diagonals:
            print("Player one(O) won!")
            self.winning_flag = 1
            return False
        if 3 in self.rows or 3 in self.columns or 3 in self.diagonals:
            print("Player two(X) won!")
            self.winning_flag = 1
            return False
        return True

    def close_connection(self):
        self.socket.close()

    def game(self):
        counter = 0
        Server.mock_board()
        print("New game started!")
        self.print_board(self)
        #first_player_play = True
        # self.winning_condition_check()
        while counter != 9:
            if counter%2==0:
                if self.first_user_move():
                    self.print_board(self)
                    counter += 1
                    print("wykonao pierwszy ruch")
            else:
                if self.second_user_move_send_board():
                    print("wyslalam spakowane dane")
                    self.second_user_move_receive_board()
                    counter += 1
        if not self.winning_flag:
            print("It's a draw!")
        print("Thanks for playing!")


new_server = Server()
new_server.connection()
new_server.game()
new_server.close_connection()
