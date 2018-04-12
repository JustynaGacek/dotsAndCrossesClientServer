# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from TCP import myEnum
from TCP.serialization import *
from ..Shared import basic
from TCP.Server.server import Server


class Server(basic.Basic):
    """ class representing the game of a dots and crosses """

    rows = [0, 0, 0]
    columns = [0, 0, 0]
    diagonals = [0, 0]
    winning_flag = 0


    TCP_PORT = 5009  # numer portu
    BUFFER_SIZE = 32
    connection = 0

    def __init__(self, connection):
        for field in range(9):
            self.board.append(' ')
        self.connection = connection

    def send_data_to_print(self, data):
        new_enum = myEnum.MyEnum()
        new_enum.header = "toPrint"
        new_enum.msg = data
        self.connection.send_data(new_enum)

    def send_info(self, data):
        new_enum = myEnum.MyEnum()
        new_enum.header = "number"
        new_enum.msg = data
        self.connection.send_data(new_enum)

    def winning_condition_increment(self, field, increment_value):
        """method used to assert how close players are to winning"""
        self.rows[math.floor(field / 3)] += increment_value
        self.columns[field % 3] += increment_value
        if field in {0, 4, 8}:
            self.diagonals[0] += increment_value
        if field in {2, 4, 6}:
            self.diagonals[1] += increment_value

    def first_user_move(self):
        try:
            field = int(input("Your turn. Choose a spot using numbers 0-8:   "))
            if self.check_if_given_field_correct(field):
                self.board[field] = "O"
                self.winning_condition_increment(field, -1)
                return True
            else:
                return False
        except ValueError:
            print("Only integers from 0 to 8 are valid.")
            self.mock_board()

    def second_user_move_send_board(self):
        self.send_info(2)
        self.send_info(self.board)
        return True

    def second_user_move_receive_board(self):
        data = self.connection.receive_data()
        field = data
        if field != '':
            field = int(field)
            self.board[field] = "X"
            self.print_board()
            self.winning_condition_increment(field, 1)

    def winning_condition_check(self):
        """method that checks winning conditions for both players"""
        if -3 in self.rows or -3 in self.columns or -3 in self.diagonals:
            print("Player one(O) won!")
            self.send_data_to_print("You lost")
            self.winning_flag = 1
            return False
        if 3 in self.rows or 3 in self.columns or 3 in self.diagonals:
            print("Player two(X) won!")
            self.send_data_to_print("You won")
            self.winning_flag = 1
            return False
        return True

    def game(self):
        counter = 0
        Server.mock_board()
        print("New game started!")
        self.send_data_to_print("Game started! Please wait for your turn")
        self.print_board()
        while counter != 9 and self.winning_condition_check():
            if counter % 2 == 0:
                if self.first_user_move():
                    self.print_board()
                    print("Second player is making a move, please wait for your turn.")
                    counter += 1
            else:
                if self.second_user_move_send_board():
                    self.send_info(1)
                    self.second_user_move_receive_board()
                    counter += 1
        if not self.winning_flag:
            print("It's a draw!")
        print("Thanks for playing!")
        self.send_data_to_print("Thanks for playing!")
        self.send_info(42)

