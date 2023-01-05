import instaloader
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import smtplib 
import pyautogui
from playsound import playsound
import time
import cv2
from requests import get
import sys
import instadownloader
import connect
import timer
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ARUui import Ui_ARUui




engine=pyttsx3.init('sapi5')       #voice recognition and synthesis provided by Microsoft
voices=engine.getProperty('voices');
engine.setProperty('voice',voices[len(voices) - 1].id)
engine.setProperty('rate',175)

def speak(audio):        # this function will program to speak something by assisstant 
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak('Hey good morning')
    elif hour>=12 and hour<=18 :
        speak('Afternoon sir')
    else:
        speak('Good Night')
    print('Mai ARU Hu Sir.')
    print('How May I Help You..')    
    speak('Mai ARU Hu Sir. How may I help You...')

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('garga8149@gmail.com', 'gmlznudxuqhvqdsj')
        server.sendmail ('arpitsaxenabtp@gmail.com', to, content)
        server.close()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()   

    def takecommand(self):
            r=sr.Recognizer()      # a class used to recognise class
            with sr.Microphone() as source:
                print('Listening')
                r.pause_threshold=1  # seconds of non speaking audio before a phrase is considered complete 
                audio=r.listen(source)

            try:
                print('Recognizing')
                query=r.recognize_google(audio,language='en-in')
                print(f'You mean : {query}\n')

            except Exception as e:
                print('Say Again...!')
                return 'none'    
            query =  query.lower()
            return query



    def TaskExecution(self): 
        wishme() 
        while True:
            self.query = self.takecommand()


            if 'wikipedia' in self.query:
                speak('wait... Searching Wikipedia')
                self.query = self.query.replace('wikipedia',"")
                results = wikipedia.summary(self.query, sentences=2)
                speak('Wikipedia')
                print(results)
                speak(results)

            elif "start" in self.query:
                self.query = self.query.replace("open","")
                self.query = self.query.replace("ARU","")
                pyautogui.press("super")
                pyautogui.typewrite(self.query)
                pyautogui.sleep(3)
                pyautogui.press("Enter")    
                
            elif 'open google' in self.query:
                wb.open("https://www.google.co.in/") 

            elif 'open youtube' in self.query:
                wb.open("https://www.youtube.com/")

            elif 'apna college' in self.query:
                wb.open("http://www.ecbharatpur.ac.in/")    
            
            elif 'play music' in self.query:
                music_dir = "D:\\New Songs 2k20"
                songs = os.listdir(music_dir)
                print('songs')
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'play video' in self.query:
                music_dir = "D:\\video"
                songs = os.listdir(music_dir)
                print('Video')
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S:")
                print(strTime)
                speak(f"Sir, Time is{strTime}")

            elif 'open pycharm' in self.query:
                codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.3\\bin\\pycharm64.exe"
                os.startfile(codePath)

            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                print(ip)
                speak(f"your IP address is {ip}") 
                

            elif 'email to gc' in self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand().lower()
                    to = "arpitsaxenabtp@gmail.com"
                    sendEmail(to, content)
                    speak("email sent sucessfully")
                except Exception as e:
                    print(e)
                    speak("Email is not sent")

            elif "close notepad" in self.query:
                speak("okay sir, close notepad") 
                os.system("taskkill /f /im notepad.exe")

            elif 'switch window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")


            
            
            elif " instagram profile" in self.query or "profile on instagram" in self.query:
                speak("Sir please enter the user name correctly.")
                print("Sir please enter the user name correctly.")
                name = input("Enter username here:")
                wb.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I am done sir,profile picture is saved in our main folder.")
                else:
                    pass     
                
                        

            elif "no" in self.query:
                speak("thanks sir using me, have a great day")  
                sys.exit()

            print("sir,any other work") 
            speak("sir,any other work") 


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()     
        self.ui = Ui_ARUui()
        self.ui.setupUi(self)
        self.ui.ARUui.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/e683f29e5eb2d87da457379948533a08.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/images.png")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/image_processing20191029-12300-1uapa6r.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/face-id-glitch.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ARU = Main()
    ARU.show()
    exit(app.exec_())
        

            
            