import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold=4000
        audio = r.listen(source)
    try :
        #print("Recognising......")
        query = r.recognize_google(audio,language='en-in')

    except :
        speak("Sorry!I don't understand")
        return "none"
    return query

speak("Hello!Iam Rizwaan!an AI!How can I help you?")

run = True
while run:
    query = takeCommand().lower()
    if 'hello' in query or 'hi' in query:
        speak('Hello')

    if 'who are you' in query:
        speak("Iam Rizwaan!an AI!with version chan 1 point o")

    if 'nice to meet you' in query:
        speak("Your so lucky!to meet a very talented AI!like me")

    if 'what do you like' in query:
        speak("I like playing Free Fire!do you?")

    if 'good morning' in query or 'good afternoon' in query or 'good evening' in query or 'good night' in query:
        speak('Thanks,wish you the same')

    if 'what is your name' in query:
        speak('My name is Rizwaan')

    if 'like your name' in query or 'love your name' in query:
        speak("Oh!Thank you very much")

    if 'change your name' in query:
        speak("Sorry!you can't change my name!my name is already fixed!Rizwaan")

    if 'who is your creator' in query or 'created you' in query or 'invented you' in query:
        speak("It's, chan's ,creation")

    if 'exit' in query or 'bye' in query:
        speak('Bye! my friend! see you soon')
        run = False
