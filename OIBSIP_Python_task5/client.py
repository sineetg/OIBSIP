import socket

HOST = '127.0.0.1'  # Same as server
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to the server.")

while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Server: {data}")

    message = input("You (client): ")
    client_socket.sendall(message.encode())

client_socket.close()
