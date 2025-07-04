import socket

HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server started. Waiting for connection on {HOST}:{PORT}...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    message = input("You (server): ")
    conn.sendall(message.encode())

    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client: {data}")

conn.close()
