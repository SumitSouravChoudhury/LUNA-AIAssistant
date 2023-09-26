import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import random
import cv2
import sys
import pyautogui
import time
import operator
import requests
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning, I am Luna. I am here to assist you.")
        speak("Good Morning, I am Luna. I am here to assist you.")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon, I am Luna. I am here to assist you.")
        speak("Good Afternoon, I am Luna. I am here to assist you.")
    else:
        print("Good Evening, I am Luna. I am here to assist you.")
        speak("Good Evening, I am Luna. I am here to assist you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query


def calculate_expression(expression):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        'x': operator.mul,
    }

    parts = expression.split()
    if len(parts) != 3:
        return "Invalid expression"

    operand1, operator_symbol, operand2 = parts

    try:
        result = operators[operator_symbol](float(operand1), float(operand2))
        return result
    except (ValueError, ZeroDivisionError) as e:
        return "Error: " + str(e)


if __name__ == "__main__":

    wishMe()

    while True:

        query = takeCommand().lower()

        if "who are you" in query:
            print(
                "My name is Luna. Stands for Logical Understanding and Navigational Assistant.")
            speak(
                "My name is Luna. Stands for Logical Understanding and Navigational Assistant.")

        elif "who created you" in query:
            print("My creator is The SHIPP")
            speak("My creator is The SHIPP")

        elif "open google" in query:
            webbrowser.open_new_tab("google.com")

        elif "search in google" in query:
            speak("What should I search?")
            qry = takeCommand().lower()
            webbrowser.open_new_tab(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open_new_tab("youtube.com")

        elif "search in youtube" in query:
            speak("What would you like to watch?")
            qrry = takeCommand().lower()
            webbrowser.open_new_tab(
                f"www.youtube.com/results?search_query={qrry}")
            
        elif "open WhatsApp" in query:
            webbrowser.open_new_tab("web.whatsapp.com")
            print("WhatsApp Web is now open in your default web browser.")
            speak("WhatsApp Web is now open in your default web browser.")
            
        elif "open chat of" in query:
            name = query.replace("open chat of", "").strip()  
            pyautogui.click(x=100, y=100)  
            time.sleep(1)
            pyautogui.write(name, interval=0.1)  
            time.sleep(1)  
            pyautogui.press("enter")
            print(f"Opening chat with {name} in WhatsApp.")
            speak(f"Opening chat with {name} in WhatsApp.")

        elif "close youtube" in query:
            os.system("taskkill /f /im msedge.exe")
            os.system("taskkill /f /im chrome.exe")

        elif "close browser" in query:
            os.system("taskkill /f /im msedge.exe")

        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")

        elif "tell me a joke" in query:
            joke_url = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(joke_url)
            if response.status_code == 200:
                joke_data = response.json()
                joke_setup = joke_data["setup"]
                joke_punchline = joke_data["punchline"]
                joke = f"{joke_setup} {joke_punchline}"
                print(joke)
                speak(joke)

        elif "open new window" in query:
            pyautogui.hotkey('ctrl', 'n')

        elif "open notepad" in query:
            npath = "C:\WINDOWS\system32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "open paint" in query:
            os.startfile(
                r"C:\Users\Sumit\AppData\Local\Microsoft\WindowsApps\mspaint.exe")

        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")

        elif "tell me a joke" in query:
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif "play music" in query:
            music_dir = r"C:\Users\Sumit\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif "play a song by" in query:
            song = query.replace("play a song by", "")
            wk.playonyt(song)

        elif "close music" in query:
            os.system("taskkill /f /im vlc.exe")

        elif "close movie" in query:
            os.system("taskkill /f /im vlc.exe")

        elif "tell me the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif "shut down the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "hibernate the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(5)
                if k == 27:
                    break
                elif k == ord('c'):
                    cv2.imwrite('captured_image.jpg', img)
                    print("Image captured and saved as 'captured_image.jpg'")
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "go to sleep" in query:
            speak("I am switching off")
            sys.exit()

        elif "take screenshot" in query:
            speak("tell me a name for the file")
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot Saved")

        elif "calculate" in query:
            expression = query.replace("calculate", "")
            result = calculate_expression(expression)
            print("The result is: " + str(result))
            speak("The result is: " + str(result))

        elif "my ip address" in query:
            speak("checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip address is")
                speak(ipAdd)
            except Exception as e:
                speak("Network is weak, please try again later")

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "type" in query:
            query = query.replace("type", "")
            pyautogui.typewrite(f"{query}", 0.1)

        elif "undo" in query:
            pyautogui.hotkey('ctrl', 'z')

        elif "maximize window" in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')

        elif "minimise window" in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')

        elif "play" in query:
            vid = query.replace("play", "")
            wk.playonyt(vid)

        elif "what is" in query:
            print("Searching Wikipedia")
            speak("Searching Wikipedia")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "who is" in query:
            speak("Searching Wikipedia")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
