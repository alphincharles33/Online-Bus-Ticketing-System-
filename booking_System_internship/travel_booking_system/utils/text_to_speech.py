# text_to_speech.py
import pyttsx3

engine = pyttsx3.init()

def text_to_speech(text):
    engine.say(text)
    engine.setProperty('rate', 0)
    engine.runAndWait()
