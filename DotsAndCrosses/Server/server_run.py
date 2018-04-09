from ..Server import server
import time


new_server = server.Server()
if new_server.connection():
    new_server.game()
    time.sleep(5)
    new_server.close_connection()