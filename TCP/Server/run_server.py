from TCP.Server.server import Server
from GuessingGame import guessingGame


new_server = Server()
if new_server.connection():
    game_type = new_server.receive_data()
    if game_type == "DaC":
        print("TODO")
    elif game_type == "GG":
        new_game = guessingGame.GuessingGame(new_server)
        new_game.start_game()
    new_server.close_connection()
