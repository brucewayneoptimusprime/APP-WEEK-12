import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

# Send a message to the server
message = "Hello, Server!"
client_socket.send(message.encode())

# Close the socket
client_socket.close()
