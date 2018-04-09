from ..Client import client


new_client = client.Client()
ip = input("Please input host ip: ")
if new_client.connect(ip):
    new_client.mock_board()
    print("New game started!")
    print("Second player is making a move, please wait for your turn...")
    while new_client.receive_data():
        new_client.move()
        print("The other player is making a move, please wait for your turn...")

