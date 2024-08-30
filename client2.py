import socket

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = '127.0.0.1'
    server_port = 8000

    try:
        # Connect to the server
        client_socket.connect((server_address, server_port))
        print('Connected to the server.')

        # Send data to the server
        message = 'Hello, server!'
        client_socket.sendall(message.encode())

        # Receive data from the server
        data = client_socket.recv(1024)
        print('Received from server:', data.decode())

    except ConnectionRefusedError:
        print('Connection refused. Make sure the server is running.')

    finally:
        # Close the socket
        client_socket.close()

if __name__ == '__main__':
    main()