import urllib.request

file = urllib.request.urlopen("https://github.com/gauravdhale09")

content = file.read()
print(content.strip())

f = open('myfile.html', 'wb')
f.write(content)
f.close()


