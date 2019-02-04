from pprint import pprint
from time import sleep
import json
import sys
import os

directory="./Data"
teams={}
"""
teams {
    name:teamname,
    penalties: num
    penaltiesyard: num
    win:
    loss:

}
"""
for filename in os.listdir(directory):
    with open(directory+"/"+filename,"r") as json_file:
        try:
            data=json.load(json_file)
        except:
            print ("Is not json "+filename) 
        else:
            for gameid in data:
                if(gameid!="nextupdate"):
                    year=gameid[0:4]
                    hometeam=data[gameid]['home']['abbr']
                    awayteam=data[gameid]['away']['abbr']
                    hometeamscore=data[gameid]['home']['score']['T']
                    awayteamscore=data[gameid]['away']['score']['T']
                    if(not(hometeam in teams.keys())):
                        teams[hometeam]={}
                        teams[hometeam]['penalties']=0
                        teams[hometeam]['penaltiesyard']=0
                        teams[hometeam]['win']=0
                        teams[hometeam]['loss']=0
                    if(not(awayteam in teams.keys())):
                        teams[awayteam]={}
                        teams[awayteam]['penalties']=0
                        teams[awayteam]['penaltiesyard']=0
                        teams[awayteam]['win']=0
                        teams[awayteam]['loss']=0
                    if(awayteamscore>hometeamscore):
                        teams[awayteam]['win']+=1
                        teams[hometeam]['loss']+=1
                    if(awayteamscore<hometeamscore):
                        teams[hometeam]['win']+=1
                        teams[awayteam]['loss']+=1
                    for drives in data[gameid]['drives'].items():
                        if(drives[0]!="crntdrv"):
                            for play in drives[1]['plays'].items():
                                for player in play[1]['players']:
                                    if(play[1]['players'][player][0]['statId']==93):
                                        if(play[1]['players'][player][0]['yards']!=None):
                                            teams[play[1]['players'][player][0]['clubcode']]['penalties']+=1 
                                            teams[play[1]['players'][player][0]['clubcode']]['penaltiesyard']+=(play[1]['players'][player][0]['yards'])
                        


# pprint(teams)                    
f=open("TeamInfo.json",'w')
f.write(json.dumps(teams))
f.close()                   
                
