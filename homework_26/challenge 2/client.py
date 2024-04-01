# Import modules
import socket, threading

# Create IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Prompt user for input nickname
nickname = input("Enter your nickname: ")

# Create socket and request server for connect
client_socket = socket.socket()
client_socket.connect((SERVER_IP, SERVER_PORT))

# This function works on receiving messages
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == "Nickname":
                client_socket.send(nickname.encode())
            else:
                print(message)
        except:
            print("Error!!!")
            client_socket.close()
            break

# This function works on writing messages
def write_message():
    while True:
        text = input()
        message = f"{nickname} -> {text}"
        
        # Write chat history in file
        with open("chat.txt", "a") as chat:
            chat.write(f"{message}\n")
        client_socket.send(message.encode())

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()
write_thread = threading.Thread(target=write_message)
write_thread.start()
