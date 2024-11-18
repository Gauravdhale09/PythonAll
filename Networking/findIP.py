import socket

host = 'www.google.com'

try:
    addr = socket.gethostbyname(host)
    print("IP address: "+addr)
except socket.gaierror:
    print("website doesn't exist")