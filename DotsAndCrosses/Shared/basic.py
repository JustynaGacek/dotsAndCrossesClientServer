#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Basic(object):

    board = []

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