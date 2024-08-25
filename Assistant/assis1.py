import assis2
import datetime
import os
import subprocess
import AppOpener
import pyaudio
import pyttsx3
import vosk
from vosk import Model, KaldiRecognizer
import pywhatkit as kt
from time import strftime
engine = pyttsx3.init('sapi5')
model = Model(
    r"C:\Users\gaura\PycharmProjects\robot\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1,
                  rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
list1 = ["wordpad", "whatsapp", "brave", "excel", "microsoft store", "microsoft edge",
         "microsoft office", "task manager", "file explorer", "word", "powerpoint", "calculator"]


def tell(i):
    voices = engine.getProperty('voices')
    engine.setProperty('language', 'en-in')
    engine.setProperty('voice', voices[-5].id)
    engine.setProperty('rate', 130)
    engine.say(i)
    engine.runAndWait()

obj = assis2.Assis2()

def hear(tex):
    if "stop" in tex:
        tell("okay")
        raise SystemExit
    elif "my" in tex or "am i" in tex:
        obj.me()
    elif "your" in tex or "you" in tex:
        obj.you()
    elif "time" in tex:
        obj.htime()
    elif "date" in tex:
        obj.hdate()
    elif tex == "hi":
        tell("Hello")
    elif "lock" in tex:
        tell("locking your pc")
        obj.lock()
    elif ("internet" in tex) and ("speed" in tex):
        obj.speed()
    elif ("restart" in tex) or ("reboot" in tex):
        tell("rebooting your pc")
        obj.restart()
    elif ("shutdown" in tex) or ("close" in tex):
        tell("closing your pc")
        obj.shut()
    elif ("break" in tex) or ("sleep" in tex):
        tell("taking break")
        obj.sleep()
    elif ("send" and "mail") in tex:
        obj.email()
    elif "set timer" in tex:
        if 'hour' in tex:
            pass

    else:
        tell("")
        pass
    for i in list1:
        if ("open" in tex) and (i in tex):
            tell("opening"+i)
            AppOpener.open(i)
    for i in list1:
        if ("close" in tex) and (i in tex):
            try:
                AppOpener.close(i)
            except Exception as e:
                print("Failed to close"+i, f"because{e}")


while True:
    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text1 = text[14:-3]
        print(text1)
        hear(text1)
