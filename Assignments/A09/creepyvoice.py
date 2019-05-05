from pydub import AudioSegment
from pydub.playback import play
import requests
import os,sys
import pprint
import json
import re

def getSound(word):
    try:
        sound=AudioSegment.from_file(".//words_us/"+word+"_us.mp3", format="mp3")  
        return sound  
    except FileNotFoundError:
        url_filename = "{}--_{}_1.mp3".format(word,"us")
        # create save location with name
        sav_filename = os.path.join("words","{}_{}.mp3".format(word,"us"))
        url = "https://ssl.gstatic.com/dictionary/static/sounds/oxford/{}".format(url_filename) 
        try:
            r = requests.get(url)
            with open(sav_filename, 'wb+') as f1:
                f1.write(r.content)
            with open('word_us_urls.txt', 'a') as f2:
                f2.write(url+"\n")   
        except Exception as e:
            print("Problem requests or saving a file: "+word+" "+e)
            return None
        try:
            sound=AudioSegment.from_file(".//words_us/"+word+"_us.mp3", format="mp3")
            return sound
        except:
            print("Problem from_file():"+word)
            return None
    except:
        print("Problem: "+word)
        return None
    return None
outputfile=None
inputfile=None
for arg in sys.argv[1:]:
        k,v = arg.split('=')
        if(k=="input_file"):
            inputfile=v
        elif(k=="output_file"):
            outputfile=v
if(inputfile):
    try:
        phrase=open(inputfile,'r')
        phrase=phrase.read()
    except FileNotFoundError as e:
        print("Problem with opening file: "+e)
    phrase=re.sub('[^a-zA-Z ]','',phrase)
    words=phrase.split()
    finalsound=getSound(words[0].lower())
    for word in words[1:]:
        sound=getSound(word.lower())
        if sound!=None:
            finalsound+=sound
    play(finalsound)
    
else:
    success=True
    while(success): 
        phrase = input("--> ")
        phrase=re.sub('[^a-zA-Z ]','',phrase)
        if (phrase != "exit"): 
            words=phrase.split()
            finalsound=getSound(words[0].lower())
            for word in words[1:]:
                sound=getSound(word.lower())
                if sound!=None:
                    finalsound+=sound
            play(finalsound)
        else:
            success=False
if(outputfile):
    finalsound.export(outputfile, format="mp3")
# sound = AudioSegment.from_file(".//words_us/a_us.mp3", format="mp3")
# sound2 = AudioSegment.from_file(".//words_us/aardvark_us.mp3", format="mp3")

# play(sound+sound2)
# print('yes')

