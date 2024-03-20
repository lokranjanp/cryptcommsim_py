import os

def upload_file(client_socket, file_name):
    try:
        # Send request type to server
        client_socket.send("upload".encode())

        # Send file name and size to server
        client_socket.send(file_name.encode())
        file_size = os.path.getsize(file_name)
        client_socket.send(str(file_size).encode())

        # Send file data to server
        with open(file_name, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.send(data)

        # Receive confirmation message from server
        confirmation = client_socket.recv(1024).decode()
        print("Server:", confirmation)

    except Exception as e:
        print("Error:", e)

def handle_file_upload(client_socket):
    try:
        # Receive file name and size from client
        file_name = client_socket.recv(1024).decode()
        file_size = int(client_socket.recv(1024).decode())

        # Receive file data from client
        with open(file_name, 'wb') as file:
            received_data = 0
            while received_data < file_size:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
                received_data += len(data)

        # Send confirmation message to client
        client_socket.send("File uploaded successfully".encode())

    except Exception as e:
        print("Error:", e)
        client_socket.send("File upload failed".encode())

def handle_file_download(client_socket, file_name):
    try:
        # Check if file exists
        if os.path.exists(file_name):
            # Send file name and size to client
            client_socket.send(file_name.encode())
            file_size = os.path.getsize(file_name)
            client_socket.send(str(file_size).encode())

            # Send file data to client
            with open(file_name, 'rb') as file:
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    client_socket.send(data)

            # Send confirmation message to client
            client_socket.send("File download successful".encode())
        else:
            # Send error message to client
            client_socket.send("File not found".encode())

    except Exception as e:
        print("Error:", e)
        client_socket.send("File download failed".encode())

def download_file(client_socket, file_name):
    try:
        # Send request type to server
        client_socket.send("download".encode())

        # Send file name to server
        client_socket.send(file_name.encode())

        # Receive file name and size from server
        received_file_name = client_socket.recv(1024).decode()
        file_size = int(client_socket.recv(1024).decode())

        # Receive file data from server and save to disk
        with open(received_file_name, 'wb') as file:
            received_data = 0
            while received_data < file_size:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
                received_data += len(data)

        # Receive confirmation message from server
        confirmation = client_socket.recv(1024).decode()
        print("Server:", confirmation)

    except Exception as e:
        print("Error:", e)
