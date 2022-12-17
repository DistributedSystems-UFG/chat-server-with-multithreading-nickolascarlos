from socket  import *
import const #- addresses, port numbers etc. (a rudimentary way to replace a proper naming service)
from handleConnection import *
from concurrent.futures import ThreadPoolExecutor

# Thread pool initialization
threadPool = ThreadPoolExecutor(max_workers=10)

server_sock = socket(AF_INET, SOCK_STREAM) # socket for clients to connect to this server
server_sock.bind((const.CHAT_SERVER_HOST, const.CHAT_SERVER_PORT))
server_sock.listen(5) # may change if too many clients

print("Chat Server is ready...")

while True:
    # Get a message from a sender client
    (conn, addr) = server_sock.accept()  # returns new socket and addr. client
    threadPool.submit(handleConnection, conn)
    
    #print("Chat Server: client is connected from address " + str(addr))
    



