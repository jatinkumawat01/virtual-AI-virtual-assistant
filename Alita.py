#pip install pyttsx3
#pip install pywin32
#pip install pipwin
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
#pip install opencv-python
#pip install schedule 
#pip install keyboard
#pip install pywhatkit
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
from random import randint
import feedparser 
import smtplib 
import ctypes
import time 
import winshell 
import win32com.client as wincl 
import re
from ecapture import ecapture as ec
from PIL import Image
import cv2
from pandas import read_csv,DataFrame
import wolframalpha # to calculate strings into formula
import requests as get
import pywhatkit as kit
from whatsapp import Whatsapp
import subprocess as sp
import wlcm
engine=pyttsx3.init()
voices= engine.getProperty('voices')                     # to change voice 
engine.setProperty('voice', voices[len(voices)-2].id)    # female
engine.setProperty('rate',150)   # voice speed

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
    speak("welcome to your pc!")
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good maorning sir!")
    elif hour >=12 and hour < 18:
        speak("Good afternoon sir!")

    elif hour >=18 and hour<24 :
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    
    
    speak("I hope you will be healthy!")

    speak("let me check your pc status!")
    time.sleep(2)

    cpu()
    
    today_msg() 
    speak("okay sir! I check that no one has a birthday today") 
    Bday()
        
    speak("sir! Please tell me how can i help you")

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

        return "none"
         
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
    speak("CPU is at"+ usage + "percent")
    bettery = psutil.sensors_battery()
    speak("your pc bettery's power ")
    speak(bettery.percent)
    speak("percent")

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
    speak("time over sir")

def Bday():
    df = read_csv('bdaystu.csv',sep=',')
    df = DataFrame(df,columns=['name','mon','date','number'])

    day =datetime.datetime.now().day
    month = datetime.datetime.now().month
    Blist =[]
    Nlist=[]

    for i in range(50):
        try:
            if month ==df['mon'][i]:
                if day ==df['date'][i]:
                    Blist.append(df['name'][i])
                    Nlist.append(int(df['number'][i]))

        except:
            break
      
    if len(Blist) == 0:
        speak("sir! Nobudy's birthday today ")
    elif len(Blist) != 0:
        
        for name in Blist:
            pic(name)
            speak("sir! do you remember today "+name+"'s Birthday")
        if len(Nlist) != 0:    
            
            for number in Nlist:
                print(number)
                speak("sir can i send birthday message")    
                wish = takeCommand()
                if 'yes' in wish or 'sure' in wish or "ok" in wish:
                    speak("okay ! sir")
                    print(name)
                    msg="""Wish u a very happy birthday {} 🎂🎂🎂. tum jiyo hajaro saal🥳🥳🥳""".format(name)
                    Whatsapp(number,msg)
                else:
                    speak("okay sir!") 
                time.sleep(2)
                os.system("taskkill /f /im Microsoft.Photos.exe")    
   # elif Blist =="None":
    #    speak("sir! Nobudy's birthday today ")                   

def detail(name):
    detail1 = ".txt"
    detail2 = name + detail1
    detail3 = 'friendsD/' + detail2

    pic(name)
    file = open(detail3, "r")
    print(file.read(0))
    speak("your friend name is " + name)
    speak("look that"+ file.read(1000))

    time.sleep(1)
    os.system("taskkill /f /im Microsoft.Photos.exe")

def pic(name):
    try:
        pic1 = ".png"
        pic2 = name + pic1
        img = Image.open('friendsPic/' + pic2)
        img.show()
        
    except Exception as e:
        print(e)
        img = Image.open('friendsPic/cat.png')
        speak("photo not found")
        img.show()
        time.sleep(2)
        os.system("taskkill /f /im Microsoft.Photos.exe")
    

def SendMsg(Name, Message):
    df = read_csv('bdaystu.csv',sep=',')
    df = DataFrame(df,columns=['name','number'])
    name =Name

    Blist =[]
    Nlist= []

    for i in range(50):
        try:
            if name ==df['name'][i]:
                
                Blist.append(df['name'][i])
                Nlist.append(int(df['number'][i]))

        except:
            break
    msg=Message
    
    for number in Nlist:
        print(number)
        if number != None:
            Whatsapp(number,msg)
        else:
            speak("sir i cann't found this person")
            speak("sir say that again ")
            return None  

def today_msg():
    num = str(randint(0,18))
    detail1 = ".txt"
    detail2 = num + detail1
    detail3 = 'good thoughts/' + detail2

    file = open(detail3, "r")
    speak("Today's message is that!")
    speak(file.read(10000))
    
def webcam():
    imgcapture = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = imgcapture.read()
        cv2.imwrite("webcam/webcam.jpg",frame)
        result =False
        speak("done..")
        img = Image.open('webcam/webcam.jpg')
        img.show()
    imgcapture.release()    
    


if __name__== "__main__":
    wlcm.welcome()
    wishme()
    
    while True:
        query = takeCommand().lower()

        if query =='none':
            continue 
        elif 'time' in query:
            time1()
        
        elif 'date' in query:
            date()


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
        
        elif 'open youtube' in query:      # this query is use to open Youtube
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
        elif 'open udemy' in query:
            wb.open("https://www.udemy.com/?utm_source=adwords-brand&utm_medium=udemyads&utm_campaign=Brand-Udemy_la.EN_cc.INDIA&utm_term=_._ag_78279294239_._ad_387461093423_._de_c_._dm__._pl__._ti_kwd-310556426868_._li_1007806_._pd__._&utm_term=_._pd__._kw_udemy_._&matchtype=e&gclid=Cj0KCQiArozwBRDOARIsAHo2s7vPYDYspCtZd9wsNs4O1zu71b3KjMM-enQRMpbuaETX4aLqjKE3Z1kaAm_REALw_wcB")
            speak("opening udemy") 

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
        elif 'open notepad plus plus' in query:
            npath="C:/Program Files (x86)/Notepad++/notepad++.exe"
            os.startfile(npath)
            speak("open notepad plus plus")
        elif "close notepad plus plus" in query:
            os.system("taskkill /f /im notepad++.exe")
            speak("okay sir, closing notepad plus plus")
        elif "open command prompt" in query or "open cmd" in query:
            os.system("start cmd") 
            speak("open CMD")   
        elif "close command prompt" in query or "close cmd" in query:
            os.system("taskkill /f /im cmd.exe")
            speak("okay sir, closing CMD")

        elif "ip address" in query:
            ip=get("https://api.ipify.org").text
            speak(f'your IP address is {ip}')  
        elif "open message"in query:
            kit.sendwhatmsg("+919799623173","hello",3,22)
        elif "play song on youtube"in query:
            speak("tell me songe ")
            song = takeCommand()
            kit.playonyt(song)
        elif "open notepad"in query:
            speak("okay sir, open notepad ")
            os.system("notepad.exe")

        elif "open vlc"in query or "open vlc player" in query:
            speak("okay sir, open vlc player ")
            os.system("start vlc")

        elif "open power point"in query:
            speak("okay sir, open microsoft power point ")
            os.system("start powerpnt")
        #elif "open telegram"in query:
         #   speak("okay sir, open telegram ")
          #  os.system("start telegram")
        elif "open microsoft edge"in query:
            speak("okay sir, open microsoft edge ")
            os.system("start msedge")
        elif "open microsoft word"in query:
            speak("okay sir, open microsoft word ")
            os.system("start winword")

        elif "open microsoft excel"in query:
            speak("okay sir, open microsoft excel ")
            os.system("start excel")    
            
        elif 'play' in query:
            song = query.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)    
            

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
            speak("okay sir, closing notepad ")
        elif "switch the window" in query or "switch the windows" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "open chrome" in query:
            speak("open google chrome")
            os.system("start chrome")
            
        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")
            speak("okay sir, closing google chrome ")




     
                    
    #query for music and video        
            
        elif 'music from pc' in query or "music" in query or "play music" in query:
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
               
        elif "shutdown my pc" in query:
            speak("shutting down your pc ")
            os.system('shutdown -s') 

        elif "restart my pc" in query:
            speak("restarting your pc ")
            os.system("shutdown /r")

        elif "sleep my pc" in query:
            speak("sleeping your pc ")
            os.system("shutdown /r")
   
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
            ec.capture(0, "alita Camera ", "img.jpg") 
          
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
            ans = takeCommand().lower()
            if 'fine' in ans or 'happy' in ans or 'okey' in ans:
                speak('okey..')  
            elif 'not' in ans or 'sad' in ans or 'upset' in ans:
                speak('oh sorry..') 

        

        elif "show my friend photos" in query or "show my friend photo" in query :
            speak("tell me your friend name")
            name = takeCommand().lower()
            pic(name)

            while True:
                speak("Sir, Do you want to see another friend's photo?")
                wish = takeCommand().lower()
                if 'yes' in wish or 'sure' in wish:
                    speak("tell me your friend name")
                    name = takeCommand().lower()
                    pic(name)
                elif "no" in wish:
                    speak("okay sir")
                    speak("this mode is off")
                    break
                else:
                    speak("this mode is off")
                    break
                    
        elif "hey alita" in query or "hi alita" in query or "ok alita" in query:
            speak("hello sir")

        elif "do you know about my friends" in query or "do you know about my friend" in query:
            speak("yes  I can try ask.")
            speak("please tell me name")
            try:
                name = takeCommand().lower()
                detail(name)
            except FileNotFoundError:
                speak("i don't know this person,")

            while True:
                speak("Sir, Do you want to know about someone else?")
                wish = takeCommand().lower()
                if 'yes' in wish or 'sure' in wish:
                    speak("please tell me name")
                    try:

                        name = takeCommand().lower()
                        detail(name)
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


         
        
        elif 'wait' in  query:
            
            wait1()

        elif 'offline' in query or 'bye' in query or 'sleep' in query or 'good bye' in query:
            speak("Good bye! sir") 
            quit()
      
        elif "send message" in query or "send whatsapp message" in query:
            speak("Please tell me ! Who do you want to send whatsapp message")
            Name = takeCommand().lower()
            print(Name)
            speak("okay sir !")
            speak("tell me what do you want to send message")
            Message = takeCommand().lower()
            print(Message)
            time.sleep(1)
            speak("sir ! can i send this message")
            wish = takeCommand().lower()
            if 'yes' in wish or 'sure' in wish:
                speak("okay ! sir")
                SendMsg(Name,Message)
        
        elif "say cheese" in query:
            speak("okay ready for pic")
            speak("3! 2! 1")
            speak("cleck")
            webcam()
        elif "temperature" in query:
            try:
                res=app.query(query)
                print(next(res.result).text)
                speak(next(res.result).text)
            except:
                print("Internet connection error.")
        

        elif "create a " in query:
            query= query.replace("create a","")
            suff= query
            speak("sir please tell me file name")
            fileName= takeCommand().lower()            
            
            if "python file" in suff:
                suff=".py"
                speak("creating python file")
            elif "java file" in suff:
                suff=".java"
                speak("creating java file")
            #elif "c file" in suff:
             #   suff= ".c"
                # speak("creating c file")
            elif "text file" in suff:
                suff=".txt"
                speak("creating text file")
            elif "document file" in suff or "docx file" in suff :
                suff = ".docx"
                speak("creating document file")   
            else:
                suff = ".txt"              
        
            Fname= fileName+suff
            f= open("C:/Users/Jatin/Desktop/"+Fname, "w")
            speak(" file is created in desktop")
            f.close()
            speak("sir can i open this file")
            wish = takeCommand().lower()
            if "yes" in wish or "sure" in wish:
                if suff == ".docx":
                    speak("okay sir "+ Fname + " is open in Microsoft word")
                    programName = "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
                    fileName = "C:/Users/Jatin/Desktop/"+Fname
                    sp.Popen([programName, fileName])
                else:
                
                        
                    programName = "C:/Program Files (x86)/Notepad++/notepad++.exe"
                    speak("okay sir "+ Fname + " is open in notepad plus plus")
                    fileName= "C:/Users/Jatin/Desktop/"+Fname
                    sp.Popen([programName, fileName])
                    
            else:
                speak("okay sir this mode is off")              
        elif query=="none":
            continue
        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            wb.open(g_url+temp) 
        #print("~~~~~~")
        #ls.lsHotword_loop()

