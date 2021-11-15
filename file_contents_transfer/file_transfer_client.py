import socket
import sys

HOST, PORT = "localhost", 6666
filename = "input.txt"

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))

    file = open(filename, 'r')
    Lines = file.readlines()

    for l in Lines:
        sock.sendall(bytes(l, "utf-8"))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("Received: {}".format(received))
