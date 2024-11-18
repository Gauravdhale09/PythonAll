# send file name to the server and receive content of that file

import socket

host = 'localhost'
port = 6767

s = socket.socket()

s.connect((host, port))

filename = input("Enter file name: ")
s.send(filename.encode())
content = s.recv(1024)
print(content.decode())

s.close()