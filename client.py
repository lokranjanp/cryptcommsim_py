import socket

# Server configuration
HOST = ''
PORT = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send a message to the server
message = "Hello, server!"
client_socket.sendall(message.encode())

# Close the connection
client_socket.close()
