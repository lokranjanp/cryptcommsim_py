import socket
import ssl

# Server configuration
HOST = ''
PORT = 12345

# Creating a user menu for Client Side
def menu():
    print("1. Send a message to the server")
    print("2. Exit")
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
    print("Connected to server")

    while True:
        choice = menu()

        if choice == 1:
            message = input("Enter your message: ")
            client_socket.sendall(message.encode())

            # Receive response from the server
            response = client_socket.recv(1024)
            print("Server response:", response.decode())

        elif choice == 2:
            print("Exiting...")
            break

except ssl.SSLError as e:
    print("SSL Error:", e)
except Exception as e:
    print("Error:", e)
finally:
    # Close the connection
    client_socket.close()
