import hashlib
import mysql.connector as sql_conn


def hash_password(password):
    # Hash password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def get_auth_details(client_socket, client_address):
    init_user_res = client_socket.recv(1024)
    init_user_res = init_user_res.decode()

    init_pass_res = client_socket.recv(1024)
    init_pass_res = init_pass_res.decode()

    if fetch_auth_user(init_user_res, init_pass_res):
        print("Successfully logged. Connected to ", client_address)
        return True
    else:
        print("Wrong username/password. Check again")
        return False


def fetch_auth_user(username, password):
    try:
        db_conn = sql_conn.connect(
            host="localhost",
            user="root",
            password="loki2003",
            database="user_auth"
        )
        cursor = db_conn.cursor()

        query = "select * from users where username = '%s'" %username
        cursor.execute(query)
        response = cursor.fetchone()

        if response:
            stored_password = response[2]
            if stored_password == hash_password(password):
                return True
            return False

    except sql_conn.Error as error:
        print("Failed to connect to user_auth database")
        return False
