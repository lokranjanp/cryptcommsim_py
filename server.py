import socket
import ssl
from auth import *

# Server configuration
HOST = 'localhost'
PORT = 8080

# Creating a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrapping the socket with SSL
server_cert_path = "/Users/lokranjan/Personal/SSLcerts/servercert.pem"
server_key_path = "/Users/lokranjan/Personal/SSLcerts/serverkey.pem"
ssl_passphrase = "loki"

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=server_cert_path, keyfile=server_key_path, password=ssl_passphrase)

server_socket = ssl_context.wrap_socket(server_socket, server_side=True)

# Socket binding with port address
server_socket.bind((HOST, PORT))

# Passive Server Open
server_socket.listen(1)

print("Server is listening...")

while True:
    # Awaiting connections
    client_socket, client_address = server_socket.accept()
    if get_auth_details(client_socket, client_address):
        client_socket.sendall("User authentication passed".encode())
    else:
        client_socket.sendall("User authentication failed".encode())

    # Receiving incoming data from client
    data = client_socket.recv(1024)
    if data:
        message = data.decode()
        print("Received:", message)

    # Sending a response back to client
    message = message.swapcase()
    client_socket.sendall(message.encode())

    # Closing connection
    client_socket.close()
