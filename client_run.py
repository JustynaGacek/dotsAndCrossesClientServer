import client


new_client = client.Client()
new_client.connect()
new_client.mock_board()
print("New game started!")
while new_client.receive_date():
    new_client.move()

new_client.close_connection()