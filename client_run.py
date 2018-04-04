import client


new_client = client.Client()
ip = input("Please input host ip: ")
if new_client.connect(ip):
    new_client.mock_board()
    print("New game started!")
    while new_client.receive_data():
        new_client.move()
