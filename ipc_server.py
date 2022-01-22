import socket
import sys

HOST = '0.0.0.0'
PORT = 9002

def send_file(self, name):
  with open('./sampletest/' + name, 'rb') as handle:
    return handle.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()

  with conn:
    print('Connected by', addr)
    #f = open("mydata.txt", 'rb')
    
    while True:
      data = conn.recv(1024)
      if not data:
         break
      #data = f.read(1024)
      conn.sendall(data)
