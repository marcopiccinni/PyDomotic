# -------------------------------------------------------------------
import pyttsx3


def speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.say(text)
    engine.runAndWait()
    return
# -------------------------------------------------------------------
