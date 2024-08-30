import socket
import threading
print("Starting Client : Client1")

HOST = 'localhost'  # The server's hostname or IP address
PORT = 8000 # The same port as used by the server

client_socket = socket.socket()
client_socket.connect((HOST, PORT))

client_socket.sendall("Hello from the client 1!".encode())
