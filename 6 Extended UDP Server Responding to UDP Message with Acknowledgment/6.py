import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('', 54321)
server_socket.bind(server_address)

while True:
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    if message == "UDP Message":
        acknowledgment = "Message Received"
        server_socket.sendto(acknowledgment.encode(), client_address)
