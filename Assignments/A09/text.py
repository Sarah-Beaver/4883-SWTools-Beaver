import pyttsx3
import engineio

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)    # Aquí puedes seleccionar la velocidad de la voz
engineio.setProperty('voice',voices[2].id)

def speak(text):
    engineio.say(text)
    engineio.runAndWait()

# speak("The quick brown fox jumped over the lazy dog.")

# for voice in voices:
#    engineio.setProperty('voice', voice.id)
#    print(voice)
#    print("\n")
#    speak('fuck off griffin')

while(1): 
    phrase = input("--> ")
    if (phrase == "exit"):
        exit(0)
    speak(phrase)
    print(voices)