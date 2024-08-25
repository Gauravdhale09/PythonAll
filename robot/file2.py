import datetime
import pyaudio
import pyttsx3
import vosk
from vosk import Model, KaldiRecognizer
from time import strftime
from py1 import list1
engine = pyttsx3.init('sapi5')
model = Model(r"C:\Users\gaura\PycharmProjects\robot\vosk-model-small-hi-0.22")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1,
                  rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
def listen(i):
    voices = engine.getProperty('voices')
    engine.setProperty('language','hindi')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 130)
    engine.say(i)
    engine.runAndWait()

def speak(tex):
    if tex=='आपणे खाना खाया':
        listen('हा खाया')

while True:
    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text1 = text[14:-3]
        print(text1)
        speak(text1)
