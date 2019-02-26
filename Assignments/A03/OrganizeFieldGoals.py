"""
Course: cmps 4883
Assignemt: A03
Date: 2/6/19
Github username: bluefire8421
Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
Name: Sarah Beaver
Description: 
    gets each player with field goals and keeps track of longest, number made, number missed
"""
from pprint import pprint
from time import sleep
import json
import sys
import os

directory="./Data"
fieldGoals={}

"""
88,71,69 -missed field goals

70 - made field goals
"""
# looks through every file in ./Data where all game stats are
for filename in os.listdir(directory):
    with open(directory+"/"+filename,"r") as json_file:
        try:
            data=json.load(json_file)
        except:
            print ("Is not json "+filename) 
        else:
            for gameid in data:
                if(gameid!="nextupdate"):
                    for driveid, drive in data[gameid]['drives'].items():
                        if(driveid!='crntdrv'):
                            for playid, play in drive['plays'].items():
                                for playerid,player in play['players'].items():
                                    if(playerid!=0):
                                        for playerinfo in player:
                                            if(playerinfo['statId']==88 or playerinfo['statId']==71 or playerinfo['statId']==70 or playerinfo['statId']==69):
                                                if(not(playerid in fieldGoals.keys())):
                                                    fieldGoals[playerid]={}
                                                    fieldGoals[playerid]['name']=playerinfo['playerName']
                                                    fieldGoals[playerid]['Longest']=0
                                                    fieldGoals[playerid]['Made']=0
                                                    fieldGoals[playerid]['Missed']=0
                                                if(playerinfo['statId']==70) :
                                                    fieldGoals[playerid]['Made']+=1
                                                    if(playerinfo['yards']!=None and playerinfo['yards']>fieldGoals[playerid]['Longest']):
                                                        fieldGoals[playerid]['Longest']=playerinfo['yards']
                                                else:
                                                    fieldGoals[playerid]['Missed']+=1

                    


pprint(fieldGoals)                    
f=open("FieldGoals.json",'w')
f.write(json.dumps(fieldGoals))
f.close()                   
                
