#!/usr/bin/python3

import urllib.request
import urllib.parse
import re
import webbrowser
import pafy
import subprocess
import os
import psutil

PROCNAME = "vlc"

def youtube(query):
    query_string = urllib.parse.urlencode({"search_query" : query})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    print("http://www.youtube.com/watch?v=" + search_results[0])
    url = "http://www.youtube.com/watch?v=" + search_results[0]

    video = pafy.new(url)
    title = video.title + ".webm"
    bestaudio = video.getbestaudio()
    bestaudio.download()
    oldtitlepath = "/home/pi/computer/" + title
    os.rename(oldtitlepath, 'song.webm')
    command = "runuser -l pi -c 'cvlc --play-and-exit /home/pi/computer/song.webm'"
    subprocess.call(command, shell=True)
    endProg(command="exit")
    return

def continuePlaying():
    command = "runuser -l pi -c 'cvlc --play-and-exit /home/pi/computer/song.webm'"
    subprocess.call(command, shell=True)
    endProg(command="exit")
    return

def endProg(command):
    success()
    if "stop" or "talking" in command:
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()
                print("VLC ENDED!")
    return
