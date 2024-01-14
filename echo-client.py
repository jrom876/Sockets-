# echo-client.py
# https://realpython.com/python-sockets/

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
WLO1 = "10.0.0.147"  # Alternate interface address

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((WLO1, PORT))
    # ~ s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
