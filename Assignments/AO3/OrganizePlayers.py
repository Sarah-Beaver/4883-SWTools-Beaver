"""
Course: cmps 4883
Assignemt: A03
Date: 2/04/19
Github username: bluefire8421
Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
Name: Sarah Beaver
Description: 
    get player info and dumps it into PlayerInfo.json
"""
from pprint import pprint
from time import sleep
import json
import os
import sys

directory="./Data"
players={}

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
                    for drives, drivedata in data[gameid]['drives'].items():
                        if(drives!="crntdrv"):
                            for play, playdata in drivedata['plays'].items():
                                for player, playerdata in playdata['players'].items():
                                    if(player!="0"):
                                        for playerinfo in playerdata:
                                            if(player not in players.keys()):
                                                players[player]={}
                                                players[player]['name']=playerinfo['playerName']
                                                players[player]['teams']=[]
                                                players[player]['rushloss']=0
                                                players[player]['rushlossyards']=0
                                                players[player]['passloss']=0
                                                players[player]['droppedpass']=0 
                                            if(not(year in players[player].keys())):
                                                players[player][year]=[]
                                            if(not(playerinfo['clubcode'] in players[player]['teams'])):
                                                players[player]['teams'].append(playerinfo['clubcode']) 
                                            if(not(playerinfo['clubcode'] in players[player][year])):
                                                players[player][year].append(playerinfo['clubcode'])
                                            if(playerinfo['statId']==10 and playerinfo['yards']!=None and  playerinfo['yards']<0):
                                                players[player]['rushloss']+=1
                                                players[player]['rushlossyards']+=playerinfo['yards']
                                            if(playerinfo['statId']==15 and playerinfo['yards']!=None and  playerinfo['yards']<0):
                                                players[player]['passloss']+=1
                                            if(playerinfo['statId']==115 and ('pass incomplete' in playdata['desc'].lower()) and ('dropped' in playdata['desc'].lower())):
                                                players[player]['droppedpass']+=1

# pprint(players)                    
f=open("PlayerInfo.json",'w')
f.write(json.dumps(players))
f.close()                   
                
