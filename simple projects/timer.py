import time
from playsound import playsound
# def count(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         format =  '{:02d}:{:02d}'.format(mins,secs)
#         print(format, end='\r')
#         time.sleep(1)
#         t -= 1
#     try:
#         playsound('winner.mp3')
#     except Exception as e:
#         print(e)
#     print('stop')
# count(int(5))
t1=int(input("Enter time in minutes="))
t = t1 * 60
time.sleep(5)
try:
    playsound("Alarm Clock Alarm.mp3")
except Exception as e:
    print(e)
print('stop')