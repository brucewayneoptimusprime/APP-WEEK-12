import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

# Open and read a text file
with open('file.txt', 'r') as file:
    file_contents = file.read()

# Send the file contents to the server
client_socket.send(file_contents.encode())

# Close the socket
client_socket.close()
