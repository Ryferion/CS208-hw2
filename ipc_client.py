import socket
import sys

# HOST = '0.0.0.0'
HOST = socket.gethostbyname('ipc_server_dns_name')
PORT = 9002


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Connected!')
    f = open ("mydata.txt", "wb")
    while 1:
        data = ''
        data = s.recv(1024)
        if data == b'': 
            break
        f.write(data)
    f.close()
    # data = f.read(1024)
    #while (data):
    #    s.sendall(b'Hello! Receiving file!')
        #data = f.read(1024)

#print('Received', repr(data))
