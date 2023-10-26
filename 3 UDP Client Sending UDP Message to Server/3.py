import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 54321)

# Send a UDP message to the server
message = "UDP Message"
client_socket.sendto(message.encode(), server_address)

# Close the socket
client_socket.close()
