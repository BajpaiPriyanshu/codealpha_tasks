import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down")
            return ""
    return command.lower()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def tell_time():
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {now}")

def play_song(song):
    speak(f"Playing {song}")
    pywhatkit.playonyt(song)

def search_web(query):
    speak(f"Searching {query}")
    pywhatkit.search(query)

def main():
    while True:
        speak("I am your voice assistant...")
        speak("How can I Help you...")
        command = listen_command()
        if 'time' in command:
            tell_time()
        elif 'play' in command:
            song = command.replace('play', '').strip()
            play_song(song)
        elif 'search' in command:
            query = command.replace('search', '').strip()
            search_web(query)
        elif 'stop' in command:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand that command")


main()
