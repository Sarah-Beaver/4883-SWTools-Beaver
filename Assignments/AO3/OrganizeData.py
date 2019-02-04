from pprint import pprint
from time import sleep
import json
import os
import sys

directory="./Data"
players={}
"""
playerid {
    name:playername,
    teams:[]  list of all teams,
    year:[] list of team that year

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
                    for stuff in data[gameid]['home']['stats'].items():
                        if(stuff[0]!='team'):
                            for player in stuff[1].items():
                                if(not(player[0] in players.keys())):
                                    players[player[0]]={}
                                    players[player[0]]['name']=player[1]['name']
                                    players[player[0]]['teams']=[]
                                    players[player[0]]['rushloss']=0
                                    players[player[0]]['rushlossyards']=0
                                if(not(year in players[player[0]].keys())):
                                    players[player[0]][year]=[]
                                if(not(hometeam in players[player[0]]['teams'])):
                                    players[player[0]]['teams'].append(hometeam) 
                                if(not(hometeam in players[player[0]][year])):
                                    players[player[0]][year].append(hometeam)
                    for stuff in data[gameid]['away']['stats'].items():
                        if(stuff[0]!='team'):
                            for player in stuff[1].items():
                                # pprint(player)
                                if(not(player[0] in players.keys())):
                                    players[player[0]]={}
                                    players[player[0]]['name']=player[1]['name']
                                    players[player[0]]['teams']=[]
                                    players[player[0]]['rushloss']=0
                                    players[player[0]]['rushlossyards']=0
                                if(not(year in players[player[0]].keys())):
                                    players[player[0]][year]=[]
                                if(not(awayteam in players[player[0]]['teams'])):
                                    players[player[0]]['teams'].append(awayteam) 
                                if(not(awayteam in players[player[0]][year])):
                                    players[player[0]][year].append(awayteam)
                    for drives in data[gameid]['drives'].items():
                        if(drives[0]!="crntdrv"):
                            for play in drives[1]['plays']:
                                    for player in drives[1]['plays'][play]['players']:
                                        if(drives[1]['plays'][play]['players'][player][0]['statId']==10 and drives[1]['plays'][play]['players'][player][0]['yards']!=None and drives[1]['plays'][play]['players'][player][0]['yards']<0):
                                            players[player]['rushloss']+=1
                                            players[player]['rushlossyards']+=drives[1]['plays'][play]['players'][player][0]['yards']
                                            pprint(players[player]['rushloss'])
                                            

pprint(players)                    
f=open("PlayerInfo.json",'w')
f.write(json.dumps(players))
f.close()                   
                
