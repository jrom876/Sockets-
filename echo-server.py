
#https://realpython.com/python-sockets/
# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

WLO1 = "10.0.0.147"  # Alternate interface address

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((WLO1, PORT))
    # ~ s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            
