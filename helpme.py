#!/usr/bin/python3

import speech_recognition as sr
import subprocess

r = sr.Recognizer()

def helpint():
    subprocess.call("runuser -l pi -c 'cvlc --play-and-exit /home/pi/computer/voice/help/intro.mp3'", shell=True)

    with sr.Microphone() as source:
        print("Waiting for initialisation")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    helpreq = r.recognize_google(audio)
    response(helpreq)
    return

def response(helpreq):
    if "commands" in helpreq:
        subprocess.call("runuser -l pi -c 'cvlc --play-and-exit /home/pi/computer/voice/help/commands.mp3' ", shell=True)
    return
