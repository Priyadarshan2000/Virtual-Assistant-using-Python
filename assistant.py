import pyttsx3
import datetime
import  wikipedia as wiki
import speech_recognition as sr
import smtplib
import os
import webbrowser
import time

import pyjokes as pj

engine=pyttsx3.init()
voices=engine.getProperty('voices')

def audio(audio):
    engine.say(audio,voices[1].id)
    engine.runAndWait()
def _time():
    now=datetime.datetime.now().strftime("%H:%M:%S")
    audio("Hey the time is ")
    audio(now)
def _date():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    audio("Hey there today is")
    audio(date)
    audio(month)
    audio(year)
def _welcomeFunction():
    audio("Welcome Back Priyadarshan")
    hour=datetime.datetime.now().hour
    if hour<12:
        audio("Good Morning Sir!")
    elif hour>=12 and hour<16:
        audio("Good afternoon Sir!")
    elif hour>=16 and hour<21:
        audio("Good evening Sir!")
    else:
        audio("Good night sir!")
def _takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-In')
        print(query)
    except Exception as e:
        print(e)
        print("Did't understand you...\nPlease say again...")
        return "NONE"
    return query

def _sendEmail(to,context):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()#server request
    server.starttls()#server establishment
    server.login("EnterYourEmailId","EnterYourPassWord")
    server.sendmail("priyadarshanghosh26@gmail.com",to,context)
    server.close()
def _jokes():
    print(pj.get_joke())
    audio(pj.get_joke())

if __name__ == '__main__':
    _welcomeFunction()
    while True:
        spech=_takeCommand().lower()
        if 'time' in spech:
            _time()
        elif 'date' in spech:
            _date()

        elif 'wikipedia'in spech:
          # audio("Searching...")
            print("Searching...")
            filter=spech.replace("wikipedia"," ")
            try:
                mainQuery= wiki.summary(filter,sentences=5)
                audio("According to wikipedia")
                print(mainQuery)
                audio(mainQuery)
            except:

                audio("Your search is not aviable in wikipedia.Please say again")
                _takeCommand()


        elif 'send email' in spech:
            try:
                audio("What you want to say speak ")
                #print("What you want to say speak ")
                content=_takeCommand()
                audio("Are you sure what you what to say")
                condirmation =_takeCommand()
                if (condirmation=='yes'):
                    pass
                else:
                    _sendEmail(to,content)
                audio("Who is the receiver of the email")
                receiver=input("Enter receiver emailId: ")
                to=receiver
                _sendEmail(to,content)
                audio("Priyadarshan your email to email address %s whose content was"%receiver)
                audio(content)
                audio("Email has been sent")
                print("Done")
            except Exception as e:
                audio("Unable to send your email")
                print(e)
        elif 'search websites'  in spech:
            audio("What should I search for")
            #print("What to search for?")
            webdriver = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = _takeCommand().lower()
            webbrowser.get(webdriver).open_new_tab(search+'.com')
        elif 'search on youtube' in spech:
            audio("What do you want to watch")
            yout=_takeCommand().lower()
            audio("Opening %s on youtube"%yout)
            webbrowser.open("https://www.youtube.com/results?search_query=%s"%yout)
        elif 'search' in spech:
            audio("What do you want to search")
            google=_takeCommand().lower()
            try:
                audio("Opening Google for %s"%google)
                webbrowser.open("https://www.google.com/search?q=%s"%google)
            except:
                audio("There was an unexpected error in google")
                audio("Opening Bing for %s" % google)
                webbrowser.open("https://https://www.bing.com/search?q=%s"%google)
        elif 'joke' in spech:
            _jokes()
        elif 'word' in spech:
            audio("opening word.Please wait")
            word=r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
            os.startfile(word)
        elif 'powerpoint' in spech:
            audio("opening Microsoft Powerpoint. Please wait")
            powerpoint=r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE'
            os.startfile(powerpoint)
        elif 'excel' in spech:
            audio("opening Microsoft Excel. Please wait")
            powerpoint = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
            os.startfile(powerpoint)
        elif 'take a note' in spech:
            audio("What should I note Priyadarshan?")
            print("What should I note Priyadarshan?")
            note=_takeCommand()
            ffile=open("new.txt",'w')
            audio("Should I add date and time with it")
            time=_takeCommand()
            if "yes" in time or "yup" in time or "yo" in time:
                startTime=datetime.datetime.now().strftime("%H:%M:%S")
                ffile.write(startTime)
                ffile.write(" :- ")
                ffile.write(note)
                audio("Done")
            else:
                ffile.write(note)
                audio("Done")
        elif "read the note" in spech:
            audio("Sure Priyadarshan;")
            ffile=open("new.txt",'r')
            print(ffile.read())
            audio(ffile.read())
        elif "pause" in spech or "hault" in spech or "sleep" in spech:
            audio("you want to pause the program for how many second?")
            pause=int(input("Enter time in seconds"))
            audio("Proagramming puasing for %d seconds"%pause)
            time.sleep(pause)

        elif 'shutdown' in spech or 'exit' in spech or 'quit' in spech:
            audio("Program shutting down")
            quit()
