import urllib.request as lib
import webbrowser as browser
url1 = input("enter any url=")
weburl = lib.urlopen("https://"+url1)
url = weburl.geturl()
print("url=",url)
info = weburl.info()
print(info)
browser.open_new(url)