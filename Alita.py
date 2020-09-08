# install these Packages


#pip install pyttsx3
#pip install pywin32
#pip install SpeechRecognition
#pip install wikipedia
#pip install pyautogui
#pip install  psutil
#pip install pyjokes
#pip install feedparser
#pip install ecapture
#pip install winshell
#pip install wolframalpha
#pip install bs4
#pip install pandas







import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes 
import operator
import random
import feedparser 
import smtplib 
import ctypes
import time 
import winshell 
import win32com.client as wincl 
import re
from ecapture import ecapture as ec
from PIL import Image
import wolframalpha # to calculate strings into formula
engine=pyttsx3.init()
voices= engine.getProperty('voices')                     # to change voice 
engine.setProperty('voice', voices[len(voices)-2].id)    # female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time1():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is ") 
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")  
    speak("I am Alita")
    time1()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good maorning sir!")
    elif hour >=12 and hour < 18:
        speak("Good afternoon sir!")

    elif hour >=18 and hour<24 :
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("Alita at your service. Please tell me how can i help you")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio= r.listen(source)
    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query) 

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
         
    return query

def sendmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('jatinkumawat0113@gmail.com','jatin')
    server.sendmail('jatinkumawat0113@gmail.com',to,content)
    server.close()

def screenshot():
    name = int(round(time.time()* 1000))
    name = '{}.png'.format(name)
    time.sleep(1)
    img = pyautogui.screenshot('screenshot/'+ name)
    img.show()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    bettery = psutil.sensors_battery()
    speak("Bettery is at ")
    speak(bettery.percent)

def jokes():
    speak(pyjokes.get_joke())

def countdown(t):
    speak("your time start")
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    speak("Time over!")
    songs_dir = 'Timer'
    songs=os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[0]))

def wait1():
    
    speak('okay! i am waiting for 60 seconds')
    time.sleep(60)


if __name__== "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time1()
        
        elif 'date' in query:
            date()

        elif "hey alita" in query:
            speak("hello sir")
            speak("please tell me something")

        elif 'wikipedia' in query:    # this query is use to open and search wikipedia
            speak("Searching...")  
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)  
        
        elif 'send email' in query:     # this query is use to send your email
            try:
                speak("what should I say?")
                content= takeCommand()
                to= 'jatinkumawat0112@gmail.com'
                #sendmail(to,content)
                #speak("Email has been send")
                speak(content)
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        
        elif 'search in chrome' in query:   # this query is use to searching in chrome
            speak("What should i search ?")
            chrompath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chrompath).open_new_tab(search + '.com')
        
        elif 'open youtube' in query:     # # this query is use to open Youtube
            speak("here you go to Youtube\n") 
            wb.open("youtube.com") 
  
        elif 'open github' in query:
            wb.open("https://www.github.com")
            speak("opening github")  
        elif 'open facebook' in query:
            wb.open("https://www.facebook.com")
            speak("opening facebook")      
        elif 'open instagram' in query:
            wb.open("https://www.instagram.com")
            speak("opening instagram")    
        elif 'open google' in query:
            wb.open("https://www.google.com")
            speak("opening google")
            
        elif 'open yahoo' in query:
            wb.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            wb.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            wb.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  

        elif 'play song on gaana' in query or 'play songs on gaana' in query or 'play music on gaana' in query:
            speak("which song do you want to play")
            song = takeCommand()
            song =song.replace (" ", "-")
            print(song)
            link= 'https://gaana.com/song/'+song

            wb.open(link) 
            speak("playing song on gaana")     
             
        elif 'open amazon' in query or 'shop online' in query:
            wb.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query:
            wb.open("https://www.flipkart.com")
            speak("opening flipkart")   
        elif 'open ebay' in query:
            wb.open("https://www.ebay.com")
            speak("opening ebay")
        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './Music'
            musics = os.listdir(music_dir)
            Mlist = [0,1,2,3,4,5,6]
            Mplay = random.choice(Mlist)
            os.startfile(os.path.join(music_dir,musics[Mplay]))
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './Video'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[0]))  
  
        
        elif "what's your name" in query or "What is your name" in query: 
            speak("My friends call me Alita")
         
             
      
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s') 
            
    
        
        elif 'remember that' in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by Jatin Kumawat.")

        elif 'do you know anything' in query:
            remember= open('data.txt','w+')
            speak("you said me to remember that"+ remember.read())
        
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        
        
        elif 'cpu'in query:
            cpu()
        
        elif 'joke' in query:
            jokes()

        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            wb.open(query)  
        
        elif "who i am" in query: 
            speak("If you talk then definitely your human.")
  
  
        elif "who are you" in query: 
            speak("I am your assistant created by Jatin Kumawat") 
  
        elif 'reason for you' in query: 
            speak("I was created as a fun by jatin ") 
  
        
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            wb.open("https://www.google.co.in/maps/place/" + location + "") 
  
        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "jaanm Camera ", "img.jpg") 
          
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('nete.txt', 'w')
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("note.txt", "r")
            print(file.read()) 
            speak(file.read(1000))
        
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takecomm()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..') 

        

        elif "show my friend photos" in query or "show my friend photo" in query :
            speak("tell me your friend name")
            name = takeCommand()
            pic1 = ".png"
            pic2 = name + pic1
            img = Image.open('friendsPic/' + pic2)
            img.show()

            while True:
                speak("Sir, Do you want to see another friend's photo?")
                wish = takeCommand()
                if 'yes' in wish or 'sure' in wish:
                    speak("tell me your friend name")
                    name = takeCommand()
                    pic1 = ".png"
                    pic2 = name + pic1
                    img = Image.open('friendsPic/' + pic2)
                    img.show()
                elif "no" in wish:
                    speak("okay sir")
                    speak("this mode is off")
                    break
                else:
                    speak("this mode is off")
                    break
                    
        elif "hey alita" in query:
            speak("hello sir")

        elif "do you know about my friends" in query:
            speak("yes  I can try ask.")
            speak("please tell me name")
            try:
                name = takeCommand()
                detail1 = ".txt"
                detail2 = name + detail1
                detail3 = 'friendsD/' + detail2

                pic1 = ".png"
                pic2 = name + pic1
                img = Image.open('friendsPic/' + pic2)
                img.show()

                file = open(detail3, "r")
                print(file.read(0))
                speak("your friend name is " + name)
                speak("look that"+ file.read(1000))
            except FileNotFoundError:
                speak("i don't know this person,")

            while True:
                speak("Sir, Do you want to know about someone else?")
                wish = takeCommand()
                if 'yes' in wish or 'sure' in wish:
                    speak("please tell me name")
                    name = takeCommand()
                    try:

                        name = takeCommand()
                        detail1 = ".txt"
                        detail2 = name + detail1
                        detail3 = 'friendsD/' + detail2

                        pic1 = ".png"
                        pic2 = name + pic1
                        img = Image.open('friendsPic/' + pic2)
                        img.show()

                        file = open(detail3, "r")
                        print(file.read(0))
                        speak("your friend name is " + name)
                        speak("look that"+ file.read(1000))
                    except FileNotFoundError:
                        speak("i don't know this person,")
                elif "no" in query:
                    speak("okay sir")
                    speak("this mode is off")
                    break
                else:
                    speak("this mode is off")
                    break
        
        
        elif "start countdown" in query:
           
            speak("How many seconds to count down? please speak in numbers:")
            seconds = takeCommand()
            while not seconds.isdigit():
                speak("That wasn't an integer! please speak in numbers:")
                seconds = takeCommand() 
            seconds = int(seconds)
            countdown(seconds)


        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you") 


        elif query == 'none':
            continue 
        
        elif 'wait' in  query:
            
            wait1()

        elif 'offline' in query or 'bye' in query or 'sleep' in query or 'good bye' in query:
            speak("Good bye! sir") 
            quit()
      

        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            wb.open(g_url+temp) 




