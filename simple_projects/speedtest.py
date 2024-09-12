import math
import speedtest
import googlesearch
import pywhatkit as kt
def stest():
    test = speedtest.Speedtest()
    d = test.download()
    u = test.upload()
    kb = d / 1024
    kbu = u / 1024
    mb = kb / 1024
    mbu = kbu / 1024
    string_mb = str(mb)
    string_mbu = str(mbu)
    print("download speed=", string_mb[0:4])
    print("uplaod speed=", string_mbu[0:4])
def google():
    what = input("what you want to search on Google=")
    kt.search(what)


stest()
