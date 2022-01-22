import socket
import sys

HOST = '127.0.0.1'
PORT = 9002


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Connected!')
    f = open ("mydata.txt", "wb")
    
    data = s.recv(1024)
    if data == b'': break
    f.write(data)
    
    # data = f.read(1024)
    #while (data):
    #    s.sendall(b'Hello! Receiving file!')
        #data = f.read(1024)

#print('Received', repr(data))
