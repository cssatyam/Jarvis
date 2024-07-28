import speech_recognition as sr
import webbrowser
import pyttsx3
from youtubesearchpython import VideosSearch


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
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "") 
        # for play on youtube
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    elif "juli" in c.lower():
        speak("which song do you want to listen")
        def search_and_play_youtube(query, limit=1):
            videosSearch = VideosSearch(query, limit=limit)
            results = videosSearch.result()
            if results and 'result' in results and len(results['result']) > 0:
                first_result = results['result'][0]
                video_link = first_result['link']
                print(f"Opening: {video_link}")
                webbrowser.open(video_link)
            else:
                print("No results found.")
        with sr.Microphone() as source:
                    speak("Please say the song name")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
        search_and_play_youtube(command)
       

    elif "open github" in c.lower():
        webbrowser.open("https://github.com/cssatyam")
        
        
        
if __name__ == "__main__":
    print("initializing jarvis...")
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
                    speak("Active Jarvis...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
            
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            
            
            
            
        except Exception as e:
            print("Error {0}".format(e))

