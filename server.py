import socket
import ssl

# Server configuration
HOST = 'localhost'
PORT = 12345

# Creating a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrapping the socket with SSL
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile="/Users/lokranjan/Personal/SSLcerts/servercert.pem", keyfile="/Users/lokranjan/Personal/SSLcerts/serverkey.pem")
server_socket = ssl_context.wrap_socket(server_socket, server_side=True)

# Socket binding with port address
server_socket.bind((HOST, PORT))

# Passive Server Open
server_socket.listen(1)

print("Server is listening...")

while True:
    # Awaiting connections
    client_socket, client_address = server_socket.accept()
    print("Connected to:", client_address)

    # Receiving incoming data from client
    data = client_socket.recv(1024)
    if data:
        print("Received:", data.decode())

    # Sending a response back to client
    message = "Received by server"
    client_socket.sendall(message.encode())

    # Closing connection
    client_socket.close()
