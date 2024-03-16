import socket
import ssl

HOST = ''
PORT = 8069

client_certif = '/Users/lokranjan/Personal/SSL Certificates/client-cert.pem'
client_keyf = '/Users/lokranjan/Personal/SSL Certificates/client-key.pem'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

ssl_socket = ssl.wrap_socket(client_socket, certfile=client_certif, keyfile=client_keyf)

message = "Hello, server!"
ssl_socket.sendall(message.encode())

ssl_socket.close()
