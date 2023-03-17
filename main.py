import speech_recognition as sr
import pyaudio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
import datetime
import webbrowser
def set_reminder():
    speak("What should I remind you about?")
    text = get_audio()
    speak("When should I remind you?")
    date_text = get_audio()

    date = datetime.datetime.strptime(date_text, "%d/%m/%Y %H:%M:%S")
    now = datetime.datetime.now()

    time_delta = (date - now).total_seconds()

    if time_delta > 0:
        time.sleep(time_delta)
        speak("Reminder: " + text)
    else:
        speak("That time has already passed.")

def create_todo_list():
    speak("What do you want to add to your to-do list?")
    item = get_audio()
    with open("todo.txt", "a") as f:
        f.write("- " + item + "\n")
    speak(item + " added to to-do list.")

def search_web():
    speak("What do you want to search for?")
    query = get_audio()
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)
    speak("Here are the search results for " + query)
while True:
    command =get_audio()
    if command is None:
        speak("Helloo")
    elif "remind me" in command:
        set_reminder()
    elif "to do" in command or "to-do" in command:
        create_todo_list()
    elif "search" in command:
        search_web()
    elif "stop" in command or "shut" in command:
        break
    

    