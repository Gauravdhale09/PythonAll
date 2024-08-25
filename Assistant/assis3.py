import datetime
import time

class Auto:
    now = datetime.datetime.now().strftime("%H:%M")
    mypass = "GRD@assistant"
    print("please confirm your identity")
    password = input("Enter password here:===")

    if password == mypass:
        print("confirming identity....")
        time.sleep(5)
        print("identity confirmed")
        now = datetime.datetime.now().time()
        if 12 > now.hour >= 6:
            time.sleep(2)
            print("Good Morning boss")
        elif 17 > now.hour >= 12:
            print("Good Afternoon boss")
        elif 22 > now.hour >= 17:
            print("Good Evening boss")
        print("Your assistant is on the way")
        try:
            import assis1
        except Exception as e:
            print(f"your assistant currently facing some problem, i think there is an {e}")
    else:
        print("password incoreect")
        forgot = input("press f, if you forgot your password and want to retrieve=====")
        if forgot == "f":
            import smtplib

            print("I am sending password to registerd email")
            myemail = 'rayanbolt52@gmail.com'
            password = 'mjfm idko qize gcoj'
            reciever = "gaurajdha2004@gmail.com"
            s = smtplib.SMTP('smtp.gmail.com', 587)
            try:
                s.starttls()
                s.login(myemail, password)
            except Exception as e:
                print(f"sorry sir, I can't send email, there is an {e} error")
            sub = "Forgot Password request"
            msg = f"you sent request for retreving assistant password at time\n{now}\nThis is your password:GRD@assistant"
            msg = "Subject:{}\n\n{}".format(sub, msg)
            s.sendmail(myemail, reciever, msg)
            chk = s.ehlo()
            try:
                if chk[0] == 250:
                    print("your password is successfully sent")
                    raise SystemExit
            except Exception as e:
                print("email not sent")
                print(f"There is an {e}")
                raise SystemExit
        else:
            raise SystemExit


if __name__ == '__main__':
    obje = Auto()


