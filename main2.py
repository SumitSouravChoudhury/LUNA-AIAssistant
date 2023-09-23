import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import openai
import os

class Luna:
    def __init__(self):
        self.chat_history = ""
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.openai_api_key = "MY_API_KEY"

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def take_command(self):
        try:
            with sr.Microphone() as source:
                print('Listening...')
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
                if 'luna' in command:
                    command = command.replace('luna', '')
                    print(command)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please repeat.")
            return None
        except sr.RequestError:
            print("Could not request results. Check your network connection.")
            return None
        return command

    def read_api_key(self):
        try:
            with open("API_KEY.txt", "r") as api_key_file:
                lines = api_key_file.readlines()
                for line in lines:
                    if line.startswith("api_key="):
                        return line.strip().split("=")[1].strip('"')
        except FileNotFoundError:
            print("API_KEY.txt file not found. Please create a file named 'API_KEY.txt' containing your OpenAI API key.")
        except Exception as e:
            print(f"Error reading API key: {str(e)}")
        return None

    def chat(self, command):
        try:
            openai.api_key = self.openai_api_key
            chat_history = "\n".join(self.chat_history)
            prompt = f"Chat History:\n{chat_history}\nUser: {command}\nAI:"
            response = openai.Completion.create(
                model="text-davinci-003",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": command},
                    {"role": "assistant", "content": prompt},
                ]
            )
            response_text = response.choices[0].message["content"]
            self.talk(response_text)
            self.chat_history.append(f"User: {command}\nAI: {response_text}")
        except Exception as e:
            print(f"Error: {str(e)}")


    def run_luna(self):
        command = self.take_command()
        if not command:
            return
        if 'play' in command:
            song = command.replace('play', '')
            self.talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%H:%M %p')
            self.talk(f'Sir, the current time is {current_time}')
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            self.talk(info)
        elif 'you' in command or 'go' in command:
            self.talk("I am an AI, here to assist you.")
        elif 'reset' in command:
            self.chat_history = ""
        else:
            print("Chatting...")
            self.chat(command)

if __name__ == "__main__":
    assistant = Luna()
    assistant.talk('Good Day Sir! I am Luna, how may I assist you today?')
    while True:
        assistant.run_luna()
