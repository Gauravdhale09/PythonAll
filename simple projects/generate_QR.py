import qrcode
from PIL import Image
import pyshorteners
def code():
    link = input("Copy paste the site name=")
    short = pyshorteners.Shortener()
    x = short.tinyurl.short(link)
    print("Shorted link=",x)
    location = input("give name to png file=")
    y = qrcode.make(x)
    file_location = 'C:/Users/gaura/PycharmProjects/generated qr/' + location + '.png'
    y.save(file_location)
    print("qrcode png location",file_location)
code()
