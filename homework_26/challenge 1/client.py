import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client Socket Created")

# Create IP address and port
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

# Connect socket to server and then close
client_socket.connect((SERVER_IP, SERVER_PORT))
received_message = client_socket.recv(1024).decode()
print(received_message)
client_socket.close()