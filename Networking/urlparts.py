import urllib.parse

url = 'http://www.dreamtechpress.com:80/engineering/computer-science.html'

tpl = urllib.parse.urlparse(url)

print(tpl)

print("scheme: ",tpl.scheme)
print("net location: ", tpl.netloc)
print("Path= ", tpl.path)
print("Parameters: ", tpl.params)
print("port: ", tpl.port)
print("Total url: ", tpl.geturl())