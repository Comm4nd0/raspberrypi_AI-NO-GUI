
import speech_recognition as sr
import _thread

r = sr.Recognizer()
def listen():
    while True:
        try:
            with sr.Microphone() as source:
                print("Waiting for initialisation")
                audio = r.listen(source)
            initiate = r.recognize_google(audio)
            print(initiate)
        except Exception as e:
            print(e)
            
    return initiate

_thread.start_new_thread(listen,())
