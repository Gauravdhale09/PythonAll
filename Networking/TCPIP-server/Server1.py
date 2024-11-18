import socket

host = '192.168.232.115'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

c, addr = s.accept()

print('Connection from: ', str(addr))

c.send(b"Hello Client, how are you?")
msg = "Bye!"
c.send(msg.encode())
c.close()
