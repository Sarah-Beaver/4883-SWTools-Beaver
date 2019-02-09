"""
Course: cmps 4883
Assignemt: A03
Date: 2/04/19
Github username: bluefire8421
Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
Name: Sarah Beaver
Description: 
    gets a teams penalties, yard penalties, wins, and losses and puts into a dictionart
    dumped int TeamInfo.json
"""
from pprint import pprint
from time import sleep
import json
import sys
import os

directory="./Data"
teams={}
valid=json.load(open("Valid_Teams.json"))
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
                    year=gameid[0:4]
                    hometeam=data[gameid]['home']['abbr']
                    awayteam=data[gameid]['away']['abbr']
                    #checks if valid game if both teams are in valid
                    if(hometeam in valid.keys() and awayteam in valid.keys()):
                        hometeam=valid[hometeam]
                        awayteam=valid[awayteam]
                        hometeamscore=data[gameid]['home']['score']['T']
                        awayteamscore=data[gameid]['away']['score']['T']
                        # adds the team if not in the dictionary
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
                        # adds win or loss to correct team
                        if(awayteamscore>hometeamscore):
                            teams[awayteam]['win']+=1
                            teams[hometeam]['loss']+=1
                        if(awayteamscore<hometeamscore):
                            teams[hometeam]['win']+=1
                            teams[awayteam]['loss']+=1
                        # loops through drives, then the plays
                        for drives in data[gameid]['drives'].items():
                            if(drives[0]!="crntdrv"):
                                for play, playdata in drives[1]['plays'].items():
                                    for player in playdata['players']:
                                        if(player!="0"):
                                            for playerinfo in playdata['players'][player]:
                                                # check for penalty then adds penalty to the team and the yards
                                                if(playerinfo['statId']==93):
                                                    if(playerinfo['yards']!=None):
                                                        teams[valid[playerinfo['clubcode']]]['penalties']+=1 
                                                        teams[valid[playerinfo['clubcode']]]['penaltiesyard']+=(playerinfo['yards'])
                        


# pprint(teams)                    
f=open("TeamInfo.json",'w')
f.write(json.dumps(teams))
f.close()                   
                
