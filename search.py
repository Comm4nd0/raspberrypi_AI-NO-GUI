import urllib
from bs4 import BeautifulSoup
from google import search
import wikipedia
import wolframalpha
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

def google(query):
    #Not used yet but i might make it a fall back if wiki of wolf doesn't return any res
    for url in search(query, stop=5):
        add = url
    html = urllib.request.urlopen(add).read()
    soup = BeautifulSoup(html, "html5lib")
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text = soup.getText()

    print (visible_text)
    return visible_text

def wiki(query):
    #wiki search and return top 3 sentences
    para = wikipedia.summary(query, sentences=3)
    return para

def wolf(query):
    #wolfram search and return all text
    wolfAPIkey = config['wolfram']['apikey']
    client = wolframalpha.Client(wolfAPIkey)
    client = wolframalpha.Client("ADD YOUR API KEY HERE!")
    res = client.query(query)

    a = len(res.pods)
    resStr = ""
    for num in range(a):
        print(res.pods[num].text)
        resStr += res.pods[num].text
    return resStr
