# speechrecognition module
# pywhatkit is for automation task
# pyttsx -text to speech recognition library

import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import sys
import pyjokes
import webbrowser
from datetime import date

engine=pyttsx3.init("sapi5")
engine.setProperty("rate",150)
voices=engine.getProperty("voices")
# print(voices[1])
engine.setProperty("voice",voices[1].id)
recognizer=sr.Recognizer()

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

def run_alexa():

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print("\n")
        print("start speaking")
        engine_talk("listening...")
        recordeaudio=recognizer.listen(source)
        try:
            command=recognizer.recognize_google(recordeaudio,language="en-in")
            command=command.lower()
            if "alexa" in command:
                command=command.replace("alexa","")
                print("you said"+command)
            else:
                print("you said: "+command)

            if "hello"  in command:
                print("hello how can i help you??")
                engine_talk("hello ,how can i help you??")

            elif "who are you" in command:
                print("I am mini alexa a k a your viritual assistant master")
                engine_talk("I am mini alexa a k a your virtual assistant master.how can i help you")

            elif "can you do" in command:
                print("i can play songs on youtbe,tell you a joke,search on wikipefia,tell date and time,find your location,locate area on map,open different website like instagram,youtube,gmail,git hun,stack overflow and searches on google,How may i help  you??")
                engine_talk("i can play songs on youtbe,tell you a joke,search on wikipefia,tell date and time,find your location,locate area on map,open different website like instagram,youtube,gmail,git hun,stack overflow and searches on google,How may i help  you??")
            
            elif "play" in command:
                song=command.replace("play","")
                print("playing"+song)

                engine_talk("playing"+song)
                pywhatkit.playonyt(song)

            elif "date and time" in command:
                today=date.today()
                time=datetime.datetime.now().strftime("%I:%M %P")
                d2=today.strftime("%B %d, %Y")
                print("Today's date is",d2,"current time is ",time)
                engine_talk(" today is:"+d2)
                engine_talk("and current time is:"+time)

            elif "time and date" in command:
                today=date.today()
                time=datetime.datetime.now().strftime("%I:%M %P")
                d2=today.strftime("%B %d, %Y")
                print("Today's date is",d2,"current time is ",time)
                engine_talk(" current time is:"+time)
                engine_talk("and Today  is:"+d2)

            elif "time" in command:
                time=datetime.datetime.now().strftime("%I:%M %P")
                print("The current time is"+time)
                engine_talk("The current time is")
                engine_talk(time)

            elif "date" in command: 
                today=date.today()
                print("today's date is:"+today)

                d2=today.strftime("%B %d,%Y")
                print("Today's date is ",d2)
                engine_talk("today's date is")
                engine_talk(d2)

            elif "tell me about" in command:
                name=command.replace("tell me about","")
                info=wikipedia.summary(name,1)
                print(info)
                engine(info)
            
            elif "wikipedia" in command:
                name=command.replace("wikipedia","")
                info=wikipedia.summary(name,1)
                print(info)
                engine_talk(info)

            elif "what is" in command:
                name=command.replace("what is","")
                info=wikipedia.summary(name,1)
                print(info)
                engine_talk(info)

            elif "who is" in command:
                name=command.replace("who is","")
                info=wikipedia.summary(name,1)
                print(info)
                engine_talk(info)

            elif "what is" in command:
                search="https://www.google.com/search?q="+command
                print("here is what i found on the internet...")
                engine_talk("searching... here is what i found on the internet...")
                webbrowser.open(search)

            elif "joke" in command:
                _joke=pyjokes.get_joke()
                print(_joke)
                engine_talk(_joke)
            
            elif "search" in command:
                search="https//www.google.com/search?q="+command
                engine_talk("searching")
                webbrowser.open(search)

            elif "my location" in command:
                url="https://www.google.com/maps/search/where+am+i+?/"
                webbrowser.get().open(url)
                engine_talk("you must be somewhere near here,as per google maps")

            elif "locate" in command:
                engine_talk("locating...")
                loc=command.replace("locate","")
                if "on map" in loc:
                    loc=loc.replace("on map","")
                url="https://google.n1/maps/place/"+loc+"/&amp;"
                webbrowser.get().open(url)
                print("here is the location of "+loc)
                engine_talk("here is the location of"+loc)

            elif "on map" in command:
                engine_talk("locating....")
                loc=command.split("")
                print(loc[1])
                url="https://google.n1/maps/place/"+loc[1]+"/&amp;"
                webbrowser.get().open(url)
                print("Here is the location of"+loc[1])
                engine_talk("here is the location of"+loc[1])

            elif "location" in command:
                engine_talk("locating...")
                loc=command.replace("find location of","")
                url="https://google.n1/maps/place/"+loc+"/&amp;"
                webbrowser.get().open(url)
                print("here is the location of"+loc)
                engine_talk("here is the location of"+loc)

            elif "where is" in command:
                engine_talk("locating...")
                loc=command.replace("where is","")
                url="https://google.n1/maps/place/"+loc+"/&amp;"
                webbrowser.get().open(url)
                print("here is the location of"+loc)
                engine_talk("here is the location of"+loc)
            
            elif "bootcamps" in command:
                search="https://tathastu.twowaits.in/index.html#courses"
                engine_talk("opening boot camps")
                webbrowser.open(search)
            
            elif " boot camps" in command:
                search="https://tathastu.twowaits.in/index.html#courses"
                engine_talk("opening boot camps")
                webbrowser.open(search)
            
            elif "python bootcamp" in command:
                search="https://tathastu.twowaits.in/kickstart_python.html"
                engine_talk("showing pythonboot camp")
                webbrowser.open(search)
            
            elif "data science bootcamp" in command:
                search="https://tathastu.twowaits.in/kickstart_data_science.html"
                engine_talk("showing data science and m1 bootcamp")
                webbrowser.open(search)
            
            elif "open google" in command:
                print("opening google....")
                engine_talk("opening google...")
                webbrowser.open_new("https://www.google.co.in/")
            
            elif "gmail" in command:
                  print("opening google....")
                  engine_talk("opening gmail...")
                  webbrowser.open_new("https://www.google.com/")

            elif "open youtube" in command:
                  print("opening youtube....")
                  engine_talk("opening youtube...")
                  webbrowser.open_new("https://www.youtune.com/")

            elif "open instagram" in command:
                  print("opening instsagram....")
                  engine_talk("opening instagram...")
                  webbrowser.open_new("https://www.instagram.com/")
             
            elif "open stack overflow" in command:
                  print("opening stackoverflow....")
                  engine_talk("opening stackoverflow...")
                  webbrowser.open_new("https://stackoverflow.com/")

            elif "open github" in command:
                  print("opening github....")
                  engine_talk("opening github...")
                  webbrowser.open_new("https://github.com/")
           
            elif "bye" in command:
                print("good bye,have a nice day!!")
                engine_talk("good bye,have a nice day!!")
                sys.exit()

            elif "thank you" in command:
                print("your welcome")
                engine_talk("your welcome")

            elif "stop" in command:
                print("good bye,have a nice day!!")
                engine_talk("good bye,have a nice day!!")
                sys.exit()         
            
            elif "exit" in command:
                print("good bye,have a nice day!!")
                engine_talk("good bye,have a nice day!!")
                sys.exit()
            
            else:
                print("here is what i found on the internet...")
                engine_talk("Here is what i found on the internet...")
                search="https://www.google.com/search?q="+command
                webbrowser.open(search)

        except Exception as ex:
            print(ex)

print("clearing background noise.. please wait")
engine_talk("Clearing background noise..please wait ")
print("\n")
print("hello i am mini  alexa how can i help you??")
engine_talk("Hello i am mini alexa,how can i help you")

while True:
    run_alexa()



