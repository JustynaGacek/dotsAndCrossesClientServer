from TCP.Server.server import Server
from GuessingGame import guessingGame
from DotsAndCrosses import gamelogic

new_server = Server()
if new_server.connection():
    game_type = new_server.receive_data()
    if game_type == "DaC":
        new_game = gamelogic.GameLogic(new_server)
        new_game.game()
    elif game_type == "GG":
        new_game = guessingGame.GuessingGame(new_server)
        print("Player started playing")
        new_game.start_game()
        print("Player finished the game. Closing connection...")
    new_server.close_connection()
