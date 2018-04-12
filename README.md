# dotsAndCrossesClientServer

# Description.

This program allows to play two different games via TCP connection.

The first game is dots and crosses and it requires two players. The players make their moves using command line. Each field of the board has consecutive number from 0 to 8 and the players choose where they want to play using one of them. Game checks user inputs and gives hints upon finding a wrong one.

The second game is GuesingGame, now you can play alone. The main rule is to guess one number from range 0 to 99. During the game you will get messages if your choice is bigger, smaller or maybe on point. What's more, you will get the amazing story to read during the game.

# How to use?

To play, have one of the players run the "server_run.py", then by running "client_run.py", the second player can connect to the server by inputting server ip when prompted by the program. Afterwards, the client has to choose one game using numbers 1 or 2. When playing dots and crosses, the second player is the server, but if you chose GuesingGame you play alone as a client. Now you are starting the game!

Have fun!
