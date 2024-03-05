import socket

# Server configuration
HOST = '0.0.0.0'
PORT = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (max 5 connections in the queue)
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

# Accept connections and handle data
while True:
    # Wait for a connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive and print data
    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")

    # Close the connection
    client_socket.close()
