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
    print(string_mb[0:4])
    print(string_mbu[0:4])
def google():
    kt.search("make a google search on black dog")
google()
