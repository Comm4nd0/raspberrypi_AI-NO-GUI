This is my RaspberryPi voice control system. it's not really an AI because it doesn't learn. However, what it can do is this...

 * Send text messages
 * Send emails
 * Search wikipeida and read back info
 * Search Wolfram and read back info
 * Play music
 * Stop read-back or play-back
 
Example commands:
"computer, send a text to marco saying get down the pub now!"
"computer, send an email to cat saying i'm down the pub, be back later"
"computer, tell me about where babies come from"
"computer, what is the time in china"
"computer, play linkin park"
"computer, stop music"

computer.py in the main file so if you want to look at all the jucy bits, that's where to start.

INSTALL THESE:
sudo apt-get update && upgrade -y
sudo apt-get install proftpd
sudo pip3 install SpeechRecognition
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip3 install pyaudio
sudo apt-get install xrdp
sudo apt-get install vlc
sudo apt-get install flac
sudo apt-get install alsamixer
sudo pip3 install gtts
sudo pip3 install beautifulsoup4
sudo pip3 install google
sudo pip3 install psutil
sudo pip3 install wikipedia
sudo pip3 install wolframalpha
sudo pip3 install pafy
sudo pip3 install youtube-dl
sudo pip3 install twilio

EDIT the config.ini file with your own info i.e.:
your own google account info (must be google for this code)
create a twilio account and generate and SID, AuthToken and phone number
add your mobile numbers in
and you personal email addresses in

run computer.py and enjoy!
hint: sudo python3 computer.py
