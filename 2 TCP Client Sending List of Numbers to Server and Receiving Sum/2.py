import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

# Send a list of numbers to the server
numbers = [1, 2, 3, 4, 5]
data = ','.join(map(str, numbers))
client_socket.send(data.encode())

# Receive the sum from the server
result = client_socket.recv(1024).decode()
print("Sum from the server:", result)

# Close the socket
client_socket.close()
