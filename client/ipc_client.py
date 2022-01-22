import socket
import sys



HOST = 'docker_server'
# HOST = socket.gethostbyname('my_socket_ipc_network')
PORT = 9002


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world. IPC success!')
    data = s.recv(1024)

print('Received', repr(data))

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Connected!')
#     f = open ("mydata.txt", "wb")
#     while 1:
#         data = ''
#         data = s.recv(1024)
#         if data == b'': 
#             break
#         f.write(data)
#     f.close()
    # data = f.read(1024)
    #while (data):
    #    s.sendall(b'Hello! Receiving file!')
        #data = f.read(1024)

#print('Received', repr(data))
