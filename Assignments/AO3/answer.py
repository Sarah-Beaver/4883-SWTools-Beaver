from pprint import pprint
from time import sleep
import json
import os
import sys

f=open('PlayerInfo.json','r') 
players=json.load(f)             
                
mostTeams=[]
mostTeamNum=0
"""
playername
"""
multipleTeamYear={}
"""
    ?
"""
mostRushes=[]
numRushes=0
for player in players:
    if(len(players[player]['teams'])>mostTeamNum):
        mostTeamNum=len(players[player]['teams'])
        mostTeams=[players[player]['name']]
    elif(len(players[player]['teams'])==mostTeamNum):
        mostTeams.append(players[player]['name'])
    if(players[player]['rushloss']>numRushes):
        numRushes=players[player]['rushloss']
        mostRushes=[players[player]['name']]
    elif(players[player]['rushloss']==numRushes):
        mostRushes.append(players[player]['name'])
    for years in players[player]:
        if(years!='name' and years!='teams' and years!='rushloss'):
            if(len(players[player][years])>1):
                if(not(players[player]['name'] in multipleTeamYear.keys())):
                    multipleTeamYear[players[player]['name']]={}    

                multipleTeamYear[players[player]['name']][years]=players[player][years]
                


print("The players that played for the most teams are ")
for item in mostTeams:
    print(item+" ")
print("The players that had the most rushes for a loss")
for item in mostRushes:
    print(item)
# pprint(players)