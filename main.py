import speech_recognition as sr
import webbrowser
import pyttsx3


recognitizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open Google " in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif"open codechef" in c.lower():
        webbrowser.open("https://codechef.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        
if __name__ == "__main__":
    speak('initializing jarvis...')
    
    while True:
        # Listen for the keyword "Jarvis"
        # obtaing from the microphone 
        r = sr.Recognizer()
        print("\nRecoginze")   
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            print("You said: " + word)
            if(word.lower()=="jarvis"):
                speak("Ya")
                
                # listen the command
                with sr.Microphone() as source:
                    print("Active Jarvis...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
            
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            speak("speak again..sir..")
            
            
            
        except Exception as e:
            print("Error {0}".format(e))

