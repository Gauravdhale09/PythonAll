import pyaudio
import pyttsx3
import vosk
from vosk import Model, KaldiRecognizer
import file4
engine = pyttsx3.init('sapi5')
model = Model(r"C:\Users\gaura\PycharmProjects\robot\vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1,
                  rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


def listen(i):
    voices = engine.getProperty('voices')
    engine.setProperty('language', 'en-in')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)
    engine.say(i)
    engine.runAndWait()


def speak(tex):
    if tex == "okay stop":
        listen("okay")
        raise SystemExit
    elif "time" in tex:
        file4.time()
    elif "date" in tex:
        file4.date()
    elif tex == "hi":
        listen("Hello")
    elif ("you" or "your") in tex:
        listen("I am sika the robo")
    elif "college" in tex:
        listen("shri sant gajanan maharaj college of engineering ssgmce")
    elif ("head" or "h o d") and ("computer science" or 'c s e') in tex:
        listen("doctor s b patil")
    elif ("head" or "h o d") and "electrical" in tex:
        listen("Doctor S R Paraskar")
    elif ("head" or "h o d") and "information technology" in tex:
        listen("Doctor A S Maanekar")
    elif ("head" or "h o d") and "electronic" in tex:
        listen("Doctor M N Tibdewal")
    elif ("head" or "h o d") and "applied science" in tex:
        listen("Doctor N A Patil")
    elif ("head" or "h o d") and "mechanical" in tex:
        listen("Doctor S P Trikaal")
    elif tex == "thanks":
        listen("its my pleasure")
    elif "library" in tex:
        listen("pradnya chakshu gulaabraao granthaalayaa")
    elif "principal" in tex:
        listen("doctor s b somaani")
    elif ('vision' and 'mission') and ("computer science" or 'c s e') in tex:
        file4.cse()
    elif ("computer science" or 'c s e') and 'intake' in tex:
        listen("60 students per year")
    elif 'establish' and ('computer science' or 'cse') in tex:
        listen("computer science department established in year 1985")
    elif ('doctor p k' or 'mister j m' or 'mister a k' or 'mister s b' or 'professor c m') in tex:
        listen("he is the assistant professor in computer science department")
    elif ('miss r a' or 'miss p v' or 'miss k p') in tex:
        listen("she is the assistant professor in computer science department")
    elif 'doctor n m' in tex:
        listen("he is the assistant professor in computer science department and has specalization in Web Technology and Security")
    elif 'doctor v s' in tex:
        listen("he is the assistant professor in computer science department and has specalization in Machine Learning and Computer Vision")
    elif ('assistant professors' or 'faculty') and ("computer science" or 'c s e') in tex:
        listen("doctor n m kandoi, professor c m mankar, doctor v s mahalle, doctor p k bharne, miss k p sable, mister j m patil, mister a k shahade, miss p v deshmukh, mister s b pagrut, miss r a zamre")
    elif ('number' or 'how') and 'faculty' and ("computer science" or 'c s e') in tex:
        listen("there are 10 faculty members in computer science department")
    else:
        listen("")


while True:
    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text1 = text[14:-3]
        print(text1)
        speak(text1)
