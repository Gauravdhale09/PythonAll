import pyshorteners
try:
    link = input("Enter link=")
    short = pyshorteners.Shortener()
    x = short.tinyurl.short(link)
    print(x)
except Exception as e:
    print(e)
