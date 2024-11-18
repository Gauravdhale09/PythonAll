# program of file server that receives a file name from a client and sends the contentof the file
import socket

host = 'localhost'
port = 6767

s = socket.socket()

s.bind((host, port))

s.listen(1)

c, addr = s.accept()
print("A client accepted the connection")

fname = c.recv(1024)
fname = str(fname.decode())
print("File name received from client: "+fname)

try:
    f = open(fname, 'rb')
    content = f.read()
    c.send(content)

    print('File content sent to client')
    c.close()
except FileNotFoundError:
    c.send("File does not exist")

c.close()