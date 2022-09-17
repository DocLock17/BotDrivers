#!/usr/bin/env python3

# NOTE: requires dependencies
#sudo apt-get install python3 python3-all-dev python3-pip build-essential swig git libpulse-dev libasound2-dev libportaudio2 libportaudiocpp0 portaudio19-dev

#sudo apt install espeak -y
#sudo apt install python3-pyaudio -y
#sudo apt-get install flac

# pip3 install pyttsx3
# pip3 install simpleaudio
# pip3 install SpeechRecognition
# pip3 install pocketsphinx


mode = 'combine' # 'google', or 'sphinx' or 'combine'
# mode = 'google'


import requests
import simpleaudio as sa
import speech_recognition as sr 
import pyttsx3
import json

r = sr.Recognizer() 
 

# Function to convert text to 
# speech 
def speak_text(message):      
    # Initialize the engine 
    engine = pyttsx3.init()
    # engine.setProperty('voice', 'en-scottish') # Raspberry
    engine.setProperty('rate', 130) # Raspberry?
    # engine.setProperty('rate', 180) # mac?
    engine.say(message)  
    engine.runAndWait() 

def request_response(text):
    query = {'input':text}
    # query = {'input':randint(1000,9999)}
    # print(text)
    # response = requests.put('http://127.0.0.1:5000', params=query)
    response = requests.put('http://35.188.177.166:5000', json=query)
    # print(count,"  ", response.json()['body'])
    return response.json()['body']


speak_text("Voice Matrix Initialized")
while(1):     
      
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone(device_index=1) as source:
            MyText = ""
            SphinxText = ""
            GoogleText = ""
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source, duration=0.2) 
              
            #listens for the user's input  
            audio = r.listen(source) 

            try:  
                # Using ggogle to recognize audio 
                GoogleText = r.recognize_google(audio)
            except sr.UnknownValueError:
                pass
                # print("Audio is blank.")
                # print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

            
            GoogleText = GoogleText.lower()
            print("Google")
            print(GoogleText+"\n")

            try:  
                # Using ggogle to recognize audio 
                SphinxText = r.recognize_google(audio)
            except sr.UnknownValueError:
                pass
                # print("Audio is blank.")
                # print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

            SphinxText = SphinxText.lower()
            print("Sphinx")
            print(SphinxText+"\n")
            print("Combined")
            print(GoogleText+" "+SphinxText+"\n\n")

            if mode == 'google':
                MyText = GoogleText
            if mode == 'sphinx':
                MyText = SphinxText
            if mode == 'combine':
                MyText = GoogleText+" "+SphinxText


            if MyText != " " and MyText != "":
                print("Getting Response")
                # print(MyText)
                res = request_response(MyText)
                print(res)
                speak_text(res)


    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError: 
        print("No Speech Detected")

    except Exception as e:
        print(e)

