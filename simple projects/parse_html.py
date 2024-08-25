import requests
from bs4 import BeautifulSoup as Bsp
import webbrowser as browser
url1 = input("Enter site name=")
url= "https://www."+ url1 + ".com"
content1 = requests.get(url)
content2 = requests.head(url)
content3 = requests.post(url)
content4 = requests.put(url)
html_content = content3.content
#print(html_content)
soup = Bsp(html_content,'html.parser')

#print(soup.prettify())
title = soup.title
print(title)
print(type(title))
paras = soup.find_all('p')
print(paras)
anchors = soup.find_all('a')
print(anchors)
browser.open_new(url)


