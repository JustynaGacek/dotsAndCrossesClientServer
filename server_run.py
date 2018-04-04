import server

new_server = server.Server()
ip = input("Please input guest IP: ")
if new_server.connection(ip):
    new_server.game()
    new_server.close_connection()