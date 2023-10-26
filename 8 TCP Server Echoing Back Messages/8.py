import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('', 12345)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    
    # Echo the data back to the client
    client_socket.send(data.encode())
    
    # Close the client socket
    client_socket.close()
