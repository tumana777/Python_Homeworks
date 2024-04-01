# Import modules
import socket, threading


# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server Socket Created.")

# Create address and port
HOST = "127.0.0.1"
PORT = 12345

# Socket bind and listening
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server listening on {HOST}:{PORT}")

# Create empty lists
clients = []
nicknames = []

# This function sends messages to everyone
def broadcast(message):
    for client in clients:
        client.send(message)

# This function handles client
def handle(client_socket):
    while True:
        # Try to get message from client
        try:
            message = client_socket.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

# This function accepts client request and runs thread
def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected from {address}")

        client.send("Nickname".encode())
        nickname = client.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(client)

        print(f"{nickname} connected")
        broadcast(f"{nickname} joined the chat".encode())

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()
        
receive()