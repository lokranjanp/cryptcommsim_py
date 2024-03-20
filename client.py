import socket
import ssl
from file_transfer import *

# Server configuration
HOST = ''
PORT = 8080

# Creating a user menu for Client Side
def menu():
    print("1. Send a message to the server")
    print("2. File Transfer")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return int(choice)

# TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrapping the socket with SSL
server_cert_path = "/Users/lokranjan/Personal/SSLcerts/servercert.pem"
ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.load_verify_locations(server_cert_path)
client_socket = ssl_context.wrap_socket(client_socket, server_hostname="loki")

try:
    # Connection with server
    client_socket.connect((HOST, PORT))

    init_user_req = input("Please enter username :")
    client_socket.sendall(init_user_req.encode())
    init_pass_req = input("Please enter password :")
    client_socket.sendall(init_pass_req.encode())

    auth_status = client_socket.recv(1024)
    print(auth_status.decode())
    if auth_status.decode() == "User authentication passed":
        session = True

    while session:
        choice = menu()

        if choice == 1:
            client_socket.sendall(str(choice).encode())
            message = input("Enter message : ")
            client_socket.sendall(message.encode())
            response_message = client_socket.recv(1024)
            print(response_message.decode())

        if choice == 2:
            file_name = "example.txt"
            upload_file(client_socket, file_name)

        if choice == 3:
            session = False

except ssl.SSLError as e:
    print("SSL Error:", e)
except Exception as e:
    print("Error:", e)
finally:
    # Close the connection
    client_socket.close()
