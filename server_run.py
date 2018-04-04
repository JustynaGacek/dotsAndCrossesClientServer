import server

new_server = server.Server()
ip = input("Podaj ip do którego chcesz sie połączyć: ")
new_server.connection(ip)
new_server.game()
new_server.close_connection()