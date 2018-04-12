from TCP.Server.server import Server
from GuessingGame import guessingGame
from DotsAndCrosses.Server import server


new_server = Server()
if new_server.connection():
    game_type = new_server.receive_data()
    if game_type == "DaC":
        new_game = server.Server(new_server)
        new_game.game()
    elif game_type == "GG":
        new_game = guessingGame.GuessingGame(new_server)
        new_game.start_game()
    new_server.close_connection()
