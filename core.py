from functools import reduce

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
# from ecapture import ecapture as ec --non functional, add on later.
import wolframalpha
import json
import requests

""""
TODO
- Allow changing of voice volume, done using pyttsx3.
- Allow changing of female/male voice, done using pyttsx3.
- Add a 'stop' command to interrupt current action.
- Allow opening any website from voice command; find out if this can be done dynamically or static.
- Look into listen_in_background command for SpeechRecognition.
"""

voiceEngine = pyttsx3.init('sapi5')  # Play around with other speech APIs
voices = voiceEngine.getProperty('voices')  ########### Check this is needed?
voiceEngine.setProperty('voice', 'voices[1].id')  # voices[0] male - voices[1] female


# Function that allows the assistant to have a voice.
def speak(text):  # Maybe change?
    voiceEngine.say(text)
    voiceEngine.runAndWait()


# What the assistant says when it is activated.
def greeting():  # Change this up, change it so that 'hello assistant' (example) triggers this.
    hourTime = datetime.now().hour ###### datetime.datetime.now().hour
    if hourTime >= 0 and hourTime < 12:
        print("Good Morning")
        speak("Good Morning")
    elif hourTime >= 12 and hourTime < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")


# The command that the user has given to the assistant.
def commandGiven():
    rec = sr.Recognizer()
    with sr.Microphone() as microphone:
        userSpeechInput = rec.listen(microphone)
        try:
            humanCommand = rec.recognize_google(userSpeechInput, language='en-NZ')
        except Exception as e:
            speak("Sorry, I missed that.")
            return "None" ######### Replace "None" with None
        return humanCommand


# greeting()

if __name__ == '__main__':
    while True:
        # speak("What can I do for you?")
        # print("What can I do for you?")
        humanCommand = commandGiven().lower()
        if humanCommand == 0:
            continue

        # Activate assistant.
        if "Hey assistant" or "Hello assistant" in humanCommand:  ######### Test this
            speak(greeting())

        # Search wikipedia based on command given.
        elif 'wikipedia' in humanCommand:
            # wikiResults = wikipedia.summary(humanCommand, sentences = 3)
            wikiCommand = humanCommand.replace("wikipedia", "") # Omit 'wikipedia' from search
            wikiResults = wikipedia.summary(wikiCommand, sentences=2)  # Sentences controls how many sentences to read from wiki article
            print("According to Wikipedia")
            speak("According to Wikipedia")
            print(wikiResults)
            speak(wikiResults)

        # Opening webbrowser tab
        elif 'open youtube' in humanCommand:
            speak("Okay")
            webbrowser.open_new_tab('youtube.com')

        elif 'open google' in humanCommand:
            speak("Okay")
            webbrowser.open_new_tab('google.com')

        elif 'open linkedin' in humanCommand:
            speak("Okay")
            webbrowser.open_new_tab('linkedin.com')

        # Dynamic search.
        # searchReplace = ("search", ""), ("look up", "")
        # elif searchReplace in humanCommand:
        #     searchCommand = reduce(lambda a, kv: a.replace(*kv) ,searchReplace, commandGiven())
        #     webbrowser.open_new_tab(searchCommand)

        # Static search.
        elif "search" in humanCommand:
            searchCommand = humanCommand.replace("search", "")
            webbrowser.open_new_tab(searchCommand)

        elif "look up" in humanCommand:
            searchCommand = humanCommand.replace("look up", "")
            webbrowser.open_new_tab(searchCommand)