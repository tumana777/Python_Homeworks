import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server Socket Created.")

# Create IP address and port
HOST = "0.0.0.0"
PORT = 12345

# Bind socket and listen
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server listening on {HOST}:{PORT}")

# Connecting client continuously
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected From {addr}")
    message = "Connection established successfully!"
    client_socket.send(message.encode())
    client_socket.close()