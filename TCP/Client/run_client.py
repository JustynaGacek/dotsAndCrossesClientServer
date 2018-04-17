from TCP.Client import client
from TCP.myEnum import MyEnum
from TCP.gameTypesEnum import GameTypesEnum
from TCP.gameTypesEnum import NoSuchGame


def end_transmisson(message):
    if message == "end_game":
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
    if game_type == GameTypesEnum.DotsAndCrosses:
        new_enum.header = 'number'
        new_enum.msg = "DaC"
        new_client.send_data(new_enum)
        while end_transmisson(data):
            data = new_client.receive_data()
            if data == "input_required":
                new_enum.header = 'number'
                Flag = True
                while Flag:
                    try:
                        checker = int(input("Your move. Choose an empty field: "))
                        Flag = False
                    except ValueError:
                        print("Wrong input. Choose a field from 0 to 8 that is still free")
                        Flag = True
                new_enum.msg = checker
                new_client.send_data(new_enum)
            if check:
                print_board(data)
                check = False
            if data == 'board_next':
                check = True
        print("Game is finished, the app will now close.")

    elif game_type == GameTypesEnum.GuessingGame:
        new_enum.header = "number"
        new_enum.msg = "GG"
        new_client.send_data(new_enum)
        while end_transmisson(data):
            data = new_client.receive_data()
            if data == "number_guess":
                new_enum.header = 'number'
                new_enum.msg = input("Well then, go ahead and try to guess! ")
                new_client.send_data(new_enum)
            if data == "final":
                new_enum.header = 'number'
                new_enum.msg = input("Delete the Evil Neural Network, that is trying to destroy the world? (y/n): ")
                new_client.send_data(new_enum)
        print("Game is finished, the app will now close.")
    else:
        raise NoSuchGame(game_type)
        print("This shouldn't happen, this game doesn't exist...")
    new_client.close_connection()
