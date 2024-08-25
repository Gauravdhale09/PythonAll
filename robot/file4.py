import file4k
import datetime
from time import strftime


def cse():
    file4k.listen("Department of Computer Science & Engineering welcomes young aspirants around the globe to shape their career by developing strong technical, analytical and communication skills so that the students besides going for software industry jobs have the necessary technical foundation")


def time():
    string = strftime('%H:%M')
    now = datetime.datetime.now().time()
    if 12 >= now.hour > 6:
        file4k.listen("Good morning")
        print(string)
        file4k.listen("its" + string)
    elif 17 >= now.hour > 12:
        file4k.listen("Good afternoon")
        print(string)
        file4k.listen("its" + string)
    elif 21 >= now.hour > 17:
        file4k.listen("Good Evening")
        print(string)
        file4k.listen("its" + string)
    elif 00 >= now.hour > 21:
        file4k.listen("Good night")
        print(string)
        file4k.listen("its" + string)
    else:
        file4k.listen(string)


def date():
    date = datetime.datetime.now()
    file4k.listen(f'{date:%b %d %Y}')

