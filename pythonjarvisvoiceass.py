import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import smtplib
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understanding..")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if "hey jarvis" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is smruti"
                speechtx(name)
            elif "how old are you" in data1:
                age = "I am 35 yers old"
                speechtx(age)
            elif "tell me about real estate" in data1:
                realestate = "real estate involves legal processes"
                speechtx(realestate)
            elif "time" in data1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(current_time)
            elif "open youtube" in data1:
                webbrowser.open("https://www.youtube.com/watch?v=y_I2YOP91Is&t=7s")
            elif "open web" in data1:
                webbrowser.open("https://timesofindia.indiatimes.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language='en', category='neutral')
                speechtx(joke_1)
            elif 'play song' in data1:
                address = "C:\\Users\\Admin\\Music\\song"
                listsong = os.listdir(address)
                print(listsong)
                os.startfile(os.path.join(address, listsong[0]))
            elif 'exit' in data1:
                speechtx("Thank you")
                break

            time.sleep(3)
    else:
        print("Thanks")