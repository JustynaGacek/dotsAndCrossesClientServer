from TCP.Client import client
from TCP.myEnum import MyEnum


def end_transmisson(number):
    if number == 42:
        return False
    else:
        return True


def print_board(board):
    for field in range(9):
        if field % 3 == 0:
            print("\n-----------")
        print(" %c " % board[field], end='')
        if (field + 1) % 3 != 0:
            print("|", end='')
    print("\n-----------")

check = False
dots = ''
new_client = client.Client()
data = ''
game_type = 0
new_enum = MyEnum()
ip = input("Please input host ip: ")
if new_client.connect(ip):
    print("Connection established.")
    print("Choose which game you want to play, by typing an integer corresponding to that name:")
    print("1. Dots and Crosses (TicTacToe)")
    print("2. Guessing Game\n Note:", end=' ')
    while 1:
        print("We are both going to be stuck in a loop until you choose a valid integer." + dots)
        try:
            game_type = int(input('Choose a game: '))
            dots += ".."
        except ValueError:
            print("Only integers are valid.")
        if 0 < game_type < 3:
            break
    if game_type == 1:
        new_enum.header = 'number'
        new_enum.msg = "DaC"
        new_client.send_data(new_enum)
        while end_transmisson(data):
            data = new_client.receive_data()
            if data == 1:
                new_enum.header = 'number'
                new_enum.msg = input("Your move. Choose an empty field: ")
                new_client.send_data(new_enum)
            if check:
                print_board(data)
                check = False
            if data == 2:
                check = True

    elif game_type == 2:
        new_enum.header = "number"
        new_enum.msg = "GG"
        new_client.send_data(new_enum)
        while end_transmisson(data):
            data = new_client.receive_data()
            if data == 1:
                new_enum.header = 'number'
                new_enum.msg = input("Well then, go ahead and try to guess! ")
                new_client.send_data(new_enum)
            if data == 2:
                new_enum.header = 'number'
                new_enum.msg = input("Delete the Evil Neural Network, that is trying to destroy the world? (y/n): ")
                new_client.send_data(new_enum)
    else:
        print("This shouldn't happen, this game doesn't exist...")
    new_client.close_connection()
