import socket
import time

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Start measuring time
start_time = time.time()

# Connect to the server
client_socket.connect(server_address)

# Send a message to the server
message = "Hello, Server!"
client_socket.send(message.encode())

# Receive a response
response = client_socket.recv(1024)

# Stop measuring time
end_time = time.time()

# Calculate and display the time taken
time_taken = end_time - start_time
print("Time taken:", time_taken, "seconds")

# Close the socket
client_socket.close()
