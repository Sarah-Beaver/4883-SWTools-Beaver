import pyttsx3
import engineio
import sys
import re

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

inputfile=None
voiceId=0
for arg in sys.argv[1:]:
        k,v = arg.split('=')
        if(k=="input_file"):
            inputfile=v
        elif(k=="voiceId"):
            voiceId=v
engineio.setProperty('voice',voices[int(voiceId)].id)
print(voices[int(voiceId)])
if(inputfile):
    try:
        phrase=open(inputfile,'r')
        phrase=phrase.read()
    except FileNotFoundError as e:
        print("Problem with opening file: "+e)
    phrase=re.sub('[^a-zA-Z ]','',phrase)
    phrase=phrase.lower()
    speak(phrase)
    
else:
    while(1): 
        phrase = str(input("--> "))
        if (phrase == "exit"):
            exit(0)
        phrase=re.sub('[^a-zA-Z ]','',phrase)
        phrase=phrase.lower()
        speak(phrase)
        # print(voices)