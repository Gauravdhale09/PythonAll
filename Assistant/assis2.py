import assis1
import datetime
import os
import subprocess
import AppOpener
from time import strftime
from playsound import playsound

class Assis2:
    def htime(self):
        string = strftime('%H:%M')
        now = datetime.datetime.now().time()
        if 12 > now.hour >= 6:
            assis1.tell("good morning")
            print(string)
            assis1.tell("its" + string)
        elif 17 > now.hour >= 12:
            assis1.tell("Good afternoon")
            print(string)
            assis1.tell("its" + string)
        elif 21 > now.hour >= 17:
            assis1.tell("Good Evening")
            print(string)
            assis1.tell("its" + string)
        elif 00 >= now.hour > 21:
            assis1.tell("Good night")
            print(string)
            assis1.tell("its" + string)
        else:
            assis1.tell(string)


    def hdate(self):
        tdate = datetime.datetime.now()
        assis1.tell(f'{tdate:%b %d %Y}')


    def shut(self):
        os.system("shutdown /s 0")


    def sleep(self):
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


    def lock(self):
        subprocess.run(["rundll32", 'user32.dll', 'LockWorkStation'])


    def restart(self):
        AppOpener.close("PyCharm Community Edition 2022.2.3")
        os.system("shutdown /r /t 0")


    def close(self):
        raise SystemExit


    def me(self):
        assis1.tell("you are gaurav, my buddy")


    def you(self):
        assis1.tell("I am rayan, gaurav's friend")


    def speed(self):
        import speedtest
        try:
            test = speedtest.SpeedTest()
            assis1.tell(
                "internet speed test is in progrees, have some patience....")
            d = test.download()
            u = test.upload()
            kb = d / 1024
            kbu = u / 1024
            mb = kb / 1024
            mbu = kbu / 1024
            string_mb = str(mb)
            string_mbu = str(mbu)
            x = string_mb[0:4]
            y = string_mbu[0:4]
            assis1.tell(
                f"your internet download speed is{x} m b per second and upload speed is {y} m b per second")
            print(
                f"your internet download speed is {x} mb/s and upload speed is {y} mb/s")
        except Exception as e:
            assis1.tell(
                f"sorry sir, device is not connected to internet or there is an error{e}")


    def email(self):
        import smtplib
        assis1.tell(
            "Ok sir, I am ready to send mail, just type the email id in console")
        myemail = 'rayanbolt52@gmail.com'
        password = 'mjfm idko qize gcoj'
        reciever = input("Enter recievers email-id here= ")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        try:
            s.starttls()
            s.login(myemail, password)
        except Exception as e:
            assis1.tell(f"sorry sir, I can't send email, there is an {e} erroe")
        assis1.tell("please type the subject and message for the email")
        sub = input("Write down subject for the email=")
        msg = input("write down msg=")
        msg = "Subject:{}\n\n{}".format(sub, msg)
        s.sendmail(myemail, reciever, msg)
        chk = s.ehlo()
        if chk[0] == 250:
            assis1.tell(f"email sent to {reciever}")
        else:
            assis1.tell(
                "sorry sir, Email not sent, please recheck recievers email id")

