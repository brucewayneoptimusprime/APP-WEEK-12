import socket
import random

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 54321)

# Generate a random number
random_number = random.randint(1, 100)

# Send the random number to the server
client_socket.sendto(str(random_number).encode(), server_address)

# Receive the result from the server
result, server = client_socket.recvfrom(1024)
print("Server says the number is:", result.decode())

# Close the socket
client_socket.close()
