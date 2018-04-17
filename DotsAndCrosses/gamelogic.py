# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from TCP import myEnum
import time


class GameLogic:
    """ class representing the game of a dots and crosses """

    rows = [0, 0, 0]
    columns = [0, 0, 0]
    diagonals = [0, 0]
    winning_flag = 0

    BUFFER_SIZE = 32
    connection = 0
    board = []

    def __init__(self, connection):
        for field in range(9):
            self.board.append(' ')
        self.connection = connection

    def print_board(self):
        for field in range(9):
            if field % 3 == 0:
                print("\n-----------")
            print(" %c " % self.board[field], end='')
            if (field + 1) % 3 != 0:
                print("|", end='')
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
        self.rows[int(math.floor(field / 3))] += increment_value
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
        self.send_info("board_next")
        time.sleep(2)
        self.send_info(self.board)
        return True

    def second_user_move_receive_field(self):
        while 1:
            self.send_info("input_required")
            data = self.connection.receive_data()
            field = data
            if self.check_if_given_field_correct(data):
                self.board[field] = "X"
                self.print_board()
                self.winning_condition_increment(field, 1)
                break
            self.send_data_to_print("Please input a valid integer.")

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
        GameLogic.mock_board()
        print("New game started!")
        self.send_data_to_print("Game started! Please wait for your turn")
        self.print_board()
        while self.winning_condition_check() and counter != 9:
            if counter % 2 == 0:
                if self.first_user_move():
                    self.print_board()
                    print("Second player is making a move, please wait for your turn.")
                    counter += 1
            else:
                if self.second_user_move_send_board():
                    self.second_user_move_receive_field()
                    counter += 1
        if not self.winning_flag:
            print("It's a draw!")
        print("Thanks for playing!")
        self.second_user_move_send_board()
        time.sleep(1)
        self.send_data_to_print("Thanks for playing!")
        self.send_info("end_game")
        time.sleep(5)

