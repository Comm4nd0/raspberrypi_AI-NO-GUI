#!/usr/bin/python3

import configparser
from twilio.rest import TwilioRestClient
import smtplib

config = configparser.ConfigParser()
config.read("config.ini")

def sms(name, message):
    name = name.lower()

    accountSID = config['SMS']['accountSID']
    authToken = config['SMS']['authToken']
    twilioCli = TwilioRestClient(accountSID, authToken)
    myTwilioNumber = config['SMS']['myTwilioNumber']

    success = "Message sent to "
    numbers = {}
    for key in config['numbers']:
        num = config['numbers'][key]
        numbers.update({key:num})
    
    print("SENDING MESSAGE")
    number = numbers[name]
    success += name
    message = twilioCli.messages.create(body=message, from_=myTwilioNumber, to=number)
    return success

def email(name, message):
    name = name.lower()
    success = "Email sent to "

    emailadds = {}

    for key in config['email']:
        add = config['email'][key]
        emailadds.update({key:add})
        
    toadd = emailadds[name]
       
    smtpadd = config['emailsettings']['smtpadd']
    outemail = config['emailsettings']['outemail']
    outemailpass = config['emailsettings']['outemailpass']
        
    server = smtplib.SMTP(smtpadd)
    server.ehlo()
    server.starttls()
    server.login(outemail, outemailpass)

    msg = "\r\n".join([
        "From: CHEYENNE.HOME",
        "To: {}",
        "Subject: MESSAGE FROM HOME",
        "",
        message,
        ]).format(toadd)
    
    server.sendmail(outemail, toadd, msg)
    success += name
    return success

def call(name):
    #COMMING SOON!
    print("Dont't know how you got here :/")
