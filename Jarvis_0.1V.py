#code by R K Shakya

# packages for our ai
from asyncio import sleep
from sys import path
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import requests
import pyjokes
from bs4 import BeautifulSoup
import sys
import speedtest
from googletrans import Translator
from gtts import gTTS
from PyDictionary import PyDictionary
import random
import pywhatkit
import pyautogui
import time
from geopy.geocoders import Nominatim
from geopy import distance


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 172)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("hello I am Jarvis. Sir, Please tell me how may i help you")


def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c105a752c8844b7d9a845e479a4c269c"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = [
        "first",
        "second",
        "third",
        "fourth",
        "sixth",
        "seventh",
    ]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


def Sleep():
    speak("Ok sir    ")
    speak("Initializing sleep mode")
    pyautogui.keyDown("alt")
    pyautogui.press("f4")
    pyautogui.keyUp("alt")
    sleep(2)
    pyautogui.press("s")
    pyautogui.press("s")
    pyautogui.press("enter")


def greetings():
    li = [
        "hello sir",
        "everything is going well sir",
        "whats app sir",
        "hi",
        "namaste sir",
    ]
    a = random.choice(li)
    print(a)
    speak(a)


def takeCommand():
    # it takes commands
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # speak("Say that again please...")
        print("Say that again please...")
        query = takeCommand().lower()
    return query


if __name__ == "__main__":  # calling a function
    wishMe()
    while True:
        query = takeCommand().lower()
                                               # logic for executing searching commands
                                               # for knowing about anything
                                               
        #Eg: tell me about python language according to wikipedia
        if "wikipedia" in query or "who" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            speak("that's all Sir")

        #Eg: Give me information about Artifial inteligence
        elif "search" in query or "information" in query or "info" in query:
            speak("sir what do you want to know")
            input = takeCommand().lower()
            results = pywhatkit.info(input, lines=2)
            speak(results)
            print(result)

        #Eg: open gooogle
        elif "google" in query:
            speak("What i have to search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("here is your result, sir")

                                                       # google search
        #Eg: what is nanotechnology  
        elif "what" in query:
            import wikipedia as googleScrap

            speak("Acoording to google")
            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query, 2)
                speak(result)
            except:
                speak("no speakable data is present")

                                                       # conversation
        
        #Eg: How are u 
        elif "how are you" in query:
            speak("I am fit and fine Sir. what about you")

        elif "hello" in query:
            greetings()

        #Eg: now close the youtube
        elif "close youtube" in query:
            speak("closing youtbe")
            pyautogui.hotkey("ctrl", "f4")

        #Eg: Open the youtube
        elif "youtube" in query:
            speak("okay sir.May i serch on it for you")
            print("okay sir.May i serch on it for you")
            input = takeCommand().lower()
            if "yes" in input:
                speak("tell me  what i have to play")
                se = takeCommand()
                pywhatkit.playonyt(f"{se}")
                speak("here is your result")
            elif "no" in input:
                webbrowser.open("youtube.com")
                speak("ok,sir")
                                                         # play my favorite music......
        #Eg: close music 
        elif "close music" in query:
            pyautogui.hotkey("ctrl", "f4")
 
        #Eg: play music for me
        elif "play music" in query:  
            music_dir = "path_to_ur_music_directory"
            speak("okay")
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

                                                           # for date and time
        #Eg: tell me the time                                                  
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%p")
            speak(f"Sir, the time is {strTime}")

        elif "day" in query:
            strTime = datetime.datetime.now().strftime("%A")
            speak(f"Sir, the today's day is {strTime}")

        elif "date" in query:
            strTime = datetime.datetime.now().strftime("%d %B:%Y")
            speak(f"Sir, the today's date is {strTime}")

                                                            # temprature
        #Eg: tell me todays temperature                                         
        elif "temperature" in query:
            search = "temperature in <ENTER YOUR DISTRICT>"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")

                                                            # offline tools
        elif "close calculator" in query:
            pyautogui.hotkey("ctrl", "f4")

        elif "calculator" in query:
            speak("opening calculator")
            path = "path_to calculator.exe"
            os.startfile(path)

        elif "close camera" in query:
            pyautogui.hotkey("ctrl", "f4")

        elif "camera" in query:
            speak("opening camera Sir")
            subprocess.run("start microsoft.windows.camera:", shell=True)
            speak("let's catch this happy moment for our album")

                                                            # for fun
        #Eg: tell me a joke                                                     
        elif "joke" in query:
            speak(f"Sir i am not that funny but i have one for you")
            joke = pyjokes.get_joke("en", category="neutral")
            speak(joke)
            print(joke)  # print
            speak("sir did you like it")

        #Eg: can u give me a advice
        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = requests.get("https://api.adviceslip.com/advice").json()
            speak(advice)
            print(advice)  # print
            speak("hope you like it")

        #Eg: tell me a quote
        elif "quote" in query:
            speak(
                "sir should i tell you a random quote or tell me the name then i will tell you  his or her quotes"
            )
            input = takeCommand().lower()
            speak("okay")
            if "yes" in input or "random" in input:
                from random_word import RandomWords
                from quote import quote

                r = RandomWords()
                w = r.get_random_word()
                print("Keyword Generated: ", w)
                speak(f"{w}")

                res = quote(w, limit=1)
                print(res)
                speak(f"{res}")
            else:
                from quote import quote

                speak("please tell me the name")
                ta = takeCommand().lower()
                result = quote(ta, limit=1)
                speak(f"{result}")
                print(result)

                                                                # location
        #Eg: tell me my location                                                        
        elif "location" in query or "where we are" in query:
            speak("okay sir let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data["city"]
                country = geo_data["country"]
                speak(f"we are currently in {city} in  {country}")
            except Exception as e:
                speak("sorry sir due to network issue i am not getting location")
                pass

                                                             # for internet speed
        #Eg: calculate internet speed                                                    
        elif "internet speed" in query:
            speak("processing")
            st = speedtest.Speedtest()
            dl = st.download() / (1025 * 1025)
            up = st.upload() / (1025 * 1025)
            d = round(dl)
            u = round(up)
            speak(
                f"Sir we have {d} mb per second downloading speed and {u} mb per second uploading speed"
            )
            print(
                f"Sir we have {d} mb per second downloading speed and {u} mb per second uploading speed"
            )

                                                            # to find distance
        #Eg: can u tell me distance between 2 location                                                    
        elif "distance" in query:
            speak("tell me the location one ")
            location1 = takeCommand().lower()
            speak("now tell me the location two")
            location2 = takeCommand().lower()
            geocoder = Nominatim(user_agent="i know py")
            coordinates1 = geocoder.geocode(location1)
            coordinates2 = geocoder.geocode(location2)
            lat1, long1 = (coordinates1.latitude), (coordinates1.longitude)
            lat2, long2 = (coordinates2.latitude), (coordinates2.longitude)
            place1 = (lat1, long1)
            place2 = (lat2, long2)
            a = distance.distance(place1, place2)
            print(f"distance between {location1} and {location2} is {a}")
            speak(f"distance between {location1} and {location2} is {a}")

                                                        # Dictionary
        #Eg: tell me the meaning of glory                                               
        elif "meaning" in query or "word meanig" in query or "dictionary" in query:
            speak("okay Sir. Sir can you please tell me the word")
            input = takeCommand().lower()
            searchword = input
            speak("processing")
            try:
                myDic = PyDictionary(searchword)
                print(myDic.getMeanings())
                speak(myDic.getMeanings())
                speak("in hindi it means")
                print(myDic.translateTo("hi"))
                speak(myDic.translateTo("hi"))  # translator
                speak(
                    "thats all. Sir do you want to know the Synonyms and antonyms of this word"
                )
                input = takeCommand().lower()
                if "yes" in input:
                    speak(
                        "okay sir. sir what do you want synonym or antonym of this word"
                    )
                    input = takeCommand().lower()
                    speak("okay sir")
                    try:
                        if "synonym" in input or "synonyms" in input:
                            speak(myDic.getSynonyms())
                        elif "antonym" in input or "antonyms" in input:
                            speak(myDic.getAntonyms())
                    except:
                        speak(
                            "Sorry Sir, i didn't get the synonym or antonym of this word"
                        )

                else:
                    speak("no problem. thank you sir")
            except:
                speak(
                    "Sorry sir something went wrong while searching meaning of the word"
                )

                                                        # for IP address
        #Eg: what's my IP address                                                
        elif "ip" in query or "IP" in query:
            ip = requests.get("https://api.ipify.org").text
            speak(f"sir your ip address is {ip}")
            print(f"sir your ip address is {ip}")

                                                       # for swiching window
        #Eg: Switch the window                                              
        elif "switch the window" in query or "switch window" in query:
            speak("switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

                                                       # for fresh news
        #Eg: tell me about today's news                                             
        elif "news" in query:
            speak("please wait sir, fetching the latest news")
            news()

                                                        # to know battery percentage
        #Eg: how much charge is left                                                
        elif (
            "how much charge" in query
            or "charginging" in query
            or "how much battery" in query
        ):
            import psutil

            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system have {percentage} percentage battery")
            if percentage >= 70:
                speak("Sir we have enough battery to continue our work")
            elif percentage <= 30:
                speak("sir we have low battery")
            elif percentage <= 25:
                speak("Sir we need to connect the system to the power source")

                                                      # for controlling screen brightness
        #Eg: tell me my screen brightness                                              
        elif "screen brightness" in query or "brightness" in query:
            import screen_brightness_control as pct

            speak(
                f"sir current brightness is {pct.get_brightness()}. sir do you want to change the brightness"
            )
            input = takeCommand()
            speak("okay sir")
            try:
                if "yes" in input:
                    speak("sir how much brightness do you want.for example- 40")
                    ch = int(takeCommand())
                    try:
                        pct.set_brightness(ch)
                        speak(f"screen brightness is now {pct.get_brightness()}")
                    except:
                        speak("can you say it again")
                elif "no" in input:
                    speak("okay sir")
            except:
                speak("can you say it again")

                                                        # control sound
        #Eg: increase volume
        elif "increase volume" in query:
            pyautogui.press("volumeup")

        elif "decrease volume" in query:
            pyautogui.press("volumedown")

        elif "mute volume" in query:
            pyautogui.press("volumemute")

                                                        # to take screenshot
        #Eg: take the screenshot                                               
        elif "screenshot" in query:
            speak("please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please wait i am taking screenshot")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot done, saved in the folder")

                                                        # reminder
        #Eg: remember that i have to complete my assignment                                            
        elif "remember" in query:
            rememberMsg = query.replace("remember that", "")
            speak("you told me to remind you that:" + rememberMsg)
            remember = open("data.txt", "w")
            remember.write(rememberMsg)
            remember.close()

        #Eg: what do u remember
        elif "what do you remember" in query:
            remember = open("data.txt", "r")
            speak("you told me that" + remember.read())

                                                         # sleep mode for desktop
        #Eg: initialize the sleep mode                                               
        elif "sleep" in query or "sleep mode" in query:
            Sleep()

                                                         # for closing jarvis
        #Eg: Bye jarvis
        elif "good bye" or "goodbye" or "bye" or "stop" in query:
            speak("okay bye sir. Have a nice day")
            sys.exit()

        speak("anything else sir")
