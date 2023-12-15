import sys
import pyttsx3
import speech_recognition as sr
import wave

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def recognize_audio(audio_data):
    r = sr.Recognizer()
    audio = wave.open('audio.wav', 'wb')  # Create a temporary WAV file
    audio.setnchannels(1)  # Specify mono audio (1 channel)
    audio.setsampwidth(2)  # Specify 16-bit sample width
    audio.setframerate(44100)  # Specify the audio sample rate
    audio.writeframes(audio_data)
    audio.close()

    with sr.AudioFile('audio.wav') as source:
        print("Listening...")
        audio = r.record(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = query.replace("Luna", "")
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again please")
        return "None"

if __name__ == '__main__':
    audio_data = sys.stdin.buffer.read()  # Read audio data from standard input
    query = recognize_audio(audio_data)

    if "Luna" and "who are you" in query:
        print("My name is Luna. Stands for Logical Understanding and Navigational Assistant.")
        speak("My name is Luna. Stands for Logical Understanding and Navigational Assistant.")
