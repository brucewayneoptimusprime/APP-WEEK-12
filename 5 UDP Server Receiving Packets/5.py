import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('', 54321)
server_socket.bind(server_address)

while True:
    data, client_address = server_socket.recvfrom(1024)
    print("Received:", data.decode(), "from", client_address)
