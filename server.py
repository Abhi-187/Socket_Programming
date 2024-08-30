import threading
import socket

def handle_client(client_socket, client_address):
    # Send a greeting message to the client
    client_socket.send("Hello, client!".encode())
    # Receive a message from the client
    message = client_socket.recv(1024).decode()
    print(f"Received message: {message}")

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(5)
print("Waiting for a connection...\n")
while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    
    # Print a message when a connection is established
    print(f"Connection from {client_address} has been established!")
    
    # Create a new thread to handle the client connection
    t = threading.Thread(target=handle_client, args=(client_socket, client_address))
    t.start()