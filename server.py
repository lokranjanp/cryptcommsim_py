import socket
import ssl

# Server configurations
HOST = 'localhost'
PORT = 12345

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile="/Users/lokranjan/Personal/SSLcerts/servercert.pem", keyfile="/Users/lokranjan/Personal/SSLcerts/serverkey.pem")
server_socket = ssl_context.wrap_socket(server_socket, server_side=True)

# Bind the socket to the address
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening...")

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    print("Connected to:", client_address)

    # Receive data from the client
    data = client_socket.recv(1024)
    if data:
        print("Received:", data.decode())

    # Send a response back to the client
    message = "Received by server"
    client_socket.sendall(message.encode())

    # Close the connection
    client_socket.close()
