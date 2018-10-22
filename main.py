#!/usr/bin/python

import pyttsx
import speech_recognition as sr

if "__main__" == __name__:

    print("Allez, cause !")
    engine = pyttsx.init()
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        #engine.say(recognizer.recognize_google(audio))
        #engine.runAndWait()