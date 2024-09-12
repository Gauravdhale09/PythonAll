import time
import pyautogui as pg
limit  = int(input("Enter limit of ="))
message = input("Enter message=")
i = 0
time.sleep(2)
while i<=limit:
    pg.typewrite(message)
    pg.press("Enter")
    i=i+1
