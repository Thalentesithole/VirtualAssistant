import pyttsx3
import datetime
import speech_recognition as sr #pip install speech_recognition
import wikipedia
import webbrowser 
import os

myName = 'Siiyalo'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak('Good morning, Thalente Sithole')
    elif hour>12 and hour<18:
        speak('Good Afternoon, Thalente Sithole')
    else:
        speak('Good evening, Thalente Sithole')
    speak(f'I am {myName}, How can i help you?')

def hearMe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('You said:', query)
    except Exception:
        print('Say that again, please')
        return 'None'
    return query

if __name__ == "__main__":
    wishme()
    while True:
        hearMe()
        query = hearMe().lower()

        if 'wikipedia' in query:
            query = query.replace('wikipedia','')
            speak('Searching Wikipedia...')
            result = wikipedia.summary(query, sentences=2)
            speak('Accoding to wikipedia')
            print(result)
            speak(result)
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open instagram' in query:
            webbrowser.open('www.instagram.com')
        elif 'coding asylum' in query:
            webbrowser.open('www.youtube.com')
        elif 'play music' in query:
            music_dir = "C:\\Users\\thale\\Music\\Playlists"
            song = os.listdir(music_dir)
            speak('Playing Music...')
            song = os.path.join(music_dir, song[2])
            os.startfile(song)
        elif 'code' in query:
            os.startfile("c:\\users\\thale\\AppData\\Lacal\\Programs\\Python\\Python38")
        elif 'your pic' or 'your image' in query:
            os.startfile('C:\\Users\\thale\\OneDrive\\Pictures')
        else:
            search = 'https://www.google.com/searching?q='+query
            




