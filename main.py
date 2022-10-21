import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition

# for computer to talk
engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




#for the computer to listen
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = 'en-in')
    except Exception as e:
        print(e)
        print("Say that again Please")
        return "None"
    return query

while True:
    query  =takecommand().lower()
    print(query)

    #speak("hello i am Awi")

    if 'hi' in query or 'hey' in query or 'hello' in query or 'heyyah' in query:
        speak('Hello Sir')
    elif 'how are you' in query:
        speak('i am fine')
    elif 'who are you' in query:
        speak('i am Iris, Yoour Virtual Assistant')
    elif 'bye' in query:
        speak('see yah later')
