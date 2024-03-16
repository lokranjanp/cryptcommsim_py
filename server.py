import socket
import ssl

# Server configuration
HOST = '0.0.0.0'
PORT = 8069

server_certif = '/Users/lokranjan/Personal/SSL Certificates/server-cert.pem'
server_keyf = '/Users/lokranjan/Personal/SSL Certificates/server-key.pem'

passkey = b'LOKI'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    ssl_socket = ssl.wrap_socket(client_socket, certfile=server_certif, keyfile=server_keyf, server_side=True, passphrase=passkey)
    data = ssl_socket.recv(1024)

    print(f"Received data: {data.decode()}")

    client_socket.close()
