# a client to send and receive messages

import socket

host = 'localhost'
port = 9000

s = socket.socket()
s.connect((host, port))

strng = input("Enter data: ")

while strng != 'exit':
    s.send(strng.encode())

    data = s.recv(1024)
    data = data.decode()

    print("From server: "+data)

    strng = input("Enter data: ")

s.close()