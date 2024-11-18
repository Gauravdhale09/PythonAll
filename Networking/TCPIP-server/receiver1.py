import socket

host = '192.168.232.115'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

msg = s.recv(1024)

while msg:
    print('Received: '+ msg.decode())
    msg = s.recv(1024)

s.close()