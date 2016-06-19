#!/usr/bin/python3

from gtts import gTTS
import os
import speech_recognition as sr
import subprocess
import random
from music import youtube
from search import google, wiki, wolf
from comms import sms, email
import time
import psutil
import _thread

r = sr.Recognizer()
exitCommands = ("exit", "end", "cancel", "close", "off")
PROCNAME = "vlc"
COMMAND = " "

def speak(say):
    print("GENERATING VOICE")
    tts = gTTS(text=say, lang='en')
    tts.save("voice/temp/temp.mp3")
    voice = "runuser -l pi -c 'cvlc --play-and-exit /home/pi/computer/voice/temp/temp.mp3 &' "
    subprocess.call(voice, shell=True)
    return

def listen():
    while True:
        try:
            with sr.Microphone() as source:
                print("Waiting for initialisation")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            initiate = r.recognize_google(audio)
            keyword = initiate[:8]
            COMMAND = str(initiate[9:])
            if keyword == "computer":
                command(COMMAND)
            else:
                print ("Oh, never mind.")
        except Exception as e:
            print(e)

def command(command):
    subprocess.call("aplay /home/pi/computer/sounds/204.wav", shell=True)
    
    try:
        if command in exitCommands:
            print ("Exiting")
            listen()
        else:
            print("Sounded like you said " + command)

            if "send" in command:
                _thread.start_new_thread(communicate(command))
            if "text" in command:
                _thread.start_new_thread(communicate(command))
            if "tell me" in command:
                _thread.start_new_thread(wiki_search(command))
            if "what is" in command:
                _thread.start_new_thread(wolf_search(command))
            if "play" in command:
                play(command)
            if "stop" in command:
                endProg(command)
            startProc()
            listen()
    except:
        print("Could not understand audio")
    return

def wiki_search(command):
    pos = command.index("tell me")
    search = command[pos+6:]
    res = wiki(search)
    print(res)
    speak(res)
    return

def wolf_search(command):
    res = wolf(command)
    res = str(res)
    speak(res)
    return
    
def play(command):
    pos = command.index("play")
    query = command[pos+5:]
    youtube(query)
    return

def getnameandmess(command):
    #get name
    pos = command.index("to")
    posChop = command[pos+3:]
    space = posChop.index(" ")
    name = posChop[:space]
    #get message
    pos = command.index("saying")
    message = command[pos+7:]
    return name, message

def communicate(command):
    if "message" or "text"in command:
        name, message = getnameandmess(command)
        res = sms(name, message)
        print(res)
        speak(res)
    if "email" in command:
        name, message = getnameandmess(command)
        res = email(name, message)
        print(res)
        speak(res)
    else:
        print("unknown message type")
    return

def endProg(command):
    if "stop" or "talking" in command:
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()
    return

def startProc():
    subprocess.Popen("runuser -l pi -c 'start-pulseaudio-x11 &'", shell=True)
    print("PulseAudio STARTED")
    subprocess.Popen("runuser -l pi -c 'jack_control start &'", shell=True)
    print("JACK STARTED")
    return

startProc()
listen()

