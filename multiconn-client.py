# multiconn-client.py

# https://realpython.com/python-sockets/

import sys
import socket
import selectors
import types

HOME = "127.0.0.1"  # The server's hostname or IP address
HOST0 = "10.0.1.7"  # Alternate interface address
PORT1 = 65432  # The port used by the server
PORT2 = 64432  # The port used by the server

sel = selectors.DefaultSelector()
messages = [b"Message 1 from client.", b"Message 2 from client."]

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print(f"Starting connection {connid} to {server_addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,
            msg_total=sum(len(m) for m in messages),
            recv_total=0,
            messages=messages.copy(),
            outb=b"",
        )
        sel.register(sock, events, data=data)

# ...

def service_connection(key, mask):
     sock = key.fileobj
     data = key.data
     if mask & selectors.EVENT_READ:
         recv_data = sock.recv(1024)  # Should be ready to read
         if recv_data:
             data.outb += recv_data
             print(f"Received {recv_data!r} from connection {data.connid}")
             data.recv_total += len(recv_data)
         else:
             print(f"Closing connection {data.connid}")
         if not recv_data or data.recv_total == data.msg_total:
             print(f"Closing connection {data.connid}")
             sel.unregister(sock)
             sock.close()
     if mask & selectors.EVENT_WRITE:
         if not data.outb and data.messages:
             data.outb = data.messages.pop(0)
         if data.outb:
             print(f"Echoing {data.outb!r} to {data.addr}")
             print(f"Sending {data.outb!r} to connection {data.connid}")
             sent = sock.send(data.outb)  # Should be ready to write
             data.outb = data.outb[sent:]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOME, PORT1))
    s.sendall(b"Hello, port1")
    data = s.recv(1024)
    
    # ~ s.connect((HOST, PORT2))
    # ~ s.sendall(b"Hello, port2")
    # ~ data = s.recv(1024)

print(f"Received {data!r}")
