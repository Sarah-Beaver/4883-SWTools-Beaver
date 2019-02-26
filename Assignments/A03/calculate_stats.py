"""
Course: cmps 4883
Assignemt: A03
Date: 2/7/19
Github username: bluefire8421
Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
Name: Sarah Beaver
Description: 
    calculates the stats for nfl
    need access to all Data/{{gameid}}.json, ./FieldGoals.json, ./PlayerInfo.json, ./TeamInfo.json, ./GameIds.json
"""
from pprint import pprint
import json
import os
import sys

# PlayersMostTeams(players)
# finds the players that played on the most teams in their career
# 
# Params: 
#    players dict : contains the data on the players
# Returns: 
#    returns a list with the players who played on the most teams
#    the list contains a list with name then number of teams
#    [[playername,numberofteams],[playername,numberofteams]]
def PlayersMostTeams(players):
    mostTeams=[]
    mostTeamNum=0
    for playerid, playerdata in players.items():
        if(len(playerdata['teams'])>mostTeamNum):
            mostTeamNum=len(playerdata['teams'])
            mostTeams=[[playerdata['name'],len(playerdata['teams'])]]
        elif(len(playerdata['teams'])==mostTeamNum):
            mostTeams.append([playerdata['name'],len(playerdata['teams'])])
    return mostTeams

# MultipleTeams(players)
# finds the players that played for more than one team in a year
# 
# Params: 
#    players dict : contains the data on the players
# Returns: 
#    returns a dictionary where keys are number of teams then key is the player name and value is the year
def MultipleTeams(players):
    multipleTeamYear={}
    for playerid, playerdata in players.items():
        for years in playerdata:
            # ignoring everything else in playerdata
            if(years!='name' and years!='teams' and years!='rushloss' and years!='rushlossyards' and years!='passloss' and years!="droppedpass"):
                if(len(playerdata[years])>1):
                    if(not(len(playerdata[years]) in multipleTeamYear.keys())):
                        multipleTeamYear[len(playerdata[years])]={}
                    multipleTeamYear[len(playerdata[years])][playerdata['name']]=years
    return multipleTeamYear

# RushedYardsLost(players)
# finds the players that had the most yards rushed for a loss
# 
# Params: 
#    players dict : contains the data on the players
# Returns: 
#    returns a list within a list, inside list has name and number of yards lost in rushing
#    [[playername,yardslost],[playername,yardslost]]
def RushedYardsLost(players):
    mostRushesYards=[]
    numRushesYards=0
    for playerid, playerdata in players.items():
        if(playerdata['rushlossyards']<numRushesYards):
            numRushesYards=playerdata['rushlossyards']
            mostRushesYards=[[playerdata['name'],playerdata['rushlossyards']]]
        elif(playerdata['rushlossyards']==numRushesYards):
            mostRushesYards.append([playerdata['name'],playerdata['rushlossyards']])
    return mostRushesYards

# NumberRushesLost(players)
# finds the players that had the most rushes for a loss
# 
# Params: 
#    players dict : contains the data on the players
# Returns: 
#    returns a list within a list, inside list has name and number of rushess for a loss
#    [[playername,yardslost],[playername,yardslost]]
def NumberRushesLost(players):
    mostRushes=[]
    numRushes=0
    for player in players:
        if(players[player]['rushloss']>numRushes):
            numRushes=players[player]['rushloss']
            mostRushes=[[players[player]['name'],players[player]['rushloss']]]
        elif(players[player]['rushloss']==numRushes):
            mostRushes.append([players[player]['name'],players[player]['rushloss']])
    return mostRushes   

# NumberPassesLost(players)
# finds the players that had the most passes for a loss
# 
# Params: 
#    players dict : contains the data on the players
# Returns: 
#    returns a list within a list, inside list has name and number of passes for a loss
#    [[playername,yardslost],[playername,yardslost]]
def NumberPassesLost(players):
    mostPasses=[]
    numPasses=0
    for player in players:
        if(players[player]['passloss']>numPasses):
            numPasses=players[player]['passloss']
            mostPasses=[[players[player]['name'],players[player]['passloss']]]
        elif(players[player]['passloss']==numPasses):
            mostPasses.append([players[player]['name'],players[player]['passloss']])
    return mostPasses 

# TeamMostPenalties(teams)
# finds the team that had the most penalties
# 
# Params: 
#    teams dict : contains the data on each team
# Returns: 
#    returns a list within a list, inside list has team name and number of penalties
#    [[teamname,numpenalties],[teamnaem,numpenalties]]
def TeamMostPenalties(teams):
    mostPenalties=[]
    numPenalties=0
    for teamname,teamdata in teams.items():
        if(teamdata['penalties']>numPenalties):
            numPenalties=teamdata['penalties']
            mostPenalties=[[teamname,teamdata['penalties']]]
        elif (teamdata['penalties']==numPenalties):
            mostPenalties.append([teamname,teamdata['penalties']])
    return mostPenalties
  
# TeamPenaltiesYards(teams)
# finds the team that had the most yards lost to penalties
# 
# Params: 
#    teams dict : contains the data on each team
# Returns: 
#    returns a list within a list, inside list has team name and number of penalties
#    [[teamname,numyardslost],[teamnaem,numyardslost]]
def TeamPenaltiesYards(teams):
    mostPenaltiesYards=[]
    numPenaltiesYards=0
    for teamname,teamdata in teams.items():
        if(teamdata['penaltiesyard']>numPenaltiesYards):
            numPenaltiesYards=teamdata['penaltiesyard']
            mostPenaltiesYards=[[teamname,teamdata['penaltiesyard']]]
        elif (teamdata['penaltiesyard']==numPenaltiesYards):
            mostPenaltiesYards.append([teamname,teamdata['penaltiesyard']])
    return mostPenaltiesYards

# PenaltyCorrelation(penalyyteams,teams)
# finds the team that had the most yards lost to penalties
# 
# Params: 
#    penalyyteams list: list of teams with most penalties
#    teams dict : contains the data on each team
# Returns: 
#    
#    
def PenaltyCorrelation(penalyyteams,teams):
    leastPenalties=teams[penalyyteams[0]]['penalties']
    correlation=[[penalyyteams[0],teams[penalyyteams[0]]['win']]]
    leastPenaltiesTeam=[]
    for teamname, teamdata in teams.items():
        if(teamdata['penalties']<leastPenalties):
            leastPenalties=teamdata['penalties']
            leastPenaltiesTeam=[[teamname,teamdata['win']]]
        elif (teamdata['penalties']==leastPenalties):
            leastPenaltiesTeam.append([teamname,teamdata['win']])
    correlation.append(leastPenaltiesTeam[0])
    return correlation

# AveragePlays()
# finds the average number of plays per game
# 
# Params: 
#    
# Returns: 
#    returns the average number of plays per game 
def AveragePlays():
    gamecount=0
    playcount=0
    for filename in os.listdir('./Data'):
        with open("./Data/"+filename,"r") as json_file:
            try:
                data=json.load(json_file)
            except:
                print ("Is not json "+filename) 
            else:
                for gameid, gamedata in data.items():
                    if(gameid!="nextupdate"):
                       gamecount+=1
                       for driveid, drivedata in gamedata['drives'].items():
                            if(driveid!="crntdrv"):
                                playcount+=drivedata['numplays']
    return playcount/gamecount

# LongestFieldGoal(fieldgoals)
# finds the longest field goal made
# 
# Params: 
#    fieldgoals dict: contains players with name and fieldgoal information
# Returns: 
#    returns a list with  player name and longest field goal 
def LongestFieldGoal(fieldgoals):
    fieldGoal=[]
    LengthFieldGoal=0
    for playerid,playerdata in fieldgoals.items():
        if(playerdata['Longest']>LengthFieldGoal):
            LengthFieldGoal=playerdata['Longest']
            fieldGoal=[[playerdata['name'],playerdata['Longest']]]
        elif (playerdata['Longest']==LengthFieldGoal):
            fieldGoal.append([playerdata['name'],playerdata['Longest']])
    return fieldGoal

# MostMadeFieldGoal(fieldgoals)
# finds the player with the most field goal made
# 
# Params: 
#    fieldgoals dict: contains players with name and fieldgoal information
# Returns: 
#    returns a list with  player name and how many made field goals
def MostMadeFieldGoal(fieldgoals):
    fieldGoal=[]
    numFieldGoal=0
    for playerid,playerdata in fieldgoals.items():
        if(playerdata['Made']>numFieldGoal):
            numFieldGoal=playerdata['Made']
            fieldGoal=[[playerdata['name'],playerdata['Made']]]
        elif (playerdata['Made']==numFieldGoal):
            fieldGoal.append([playerdata['name'],playerdata['Made']])
    return fieldGoal

# MostMissedFieldGoal(fieldgoals)
# finds the most missed field goal 
# 
# Params: 
#    fieldgoals dict: contains players with name and fieldgoal information
# Returns: 
#    returns a list with  player name and how many missed field goals
def MostMissedFieldGoal(fieldgoals):
    fieldGoal=[]
    numFieldGoal=0
    for playerid,playerdata in fieldgoals.items():
        if(playerdata['Missed']>numFieldGoal):
            numFieldGoal=playerdata['Missed']
            fieldGoal=[[playerdata['name'],playerdata['Missed']]]
        elif (playerdata['Missed']==numFieldGoal):
            fieldGoal.append([playerdata['name'],playerdata['Missed']])
    return fieldGoal

# MostDroppedPasses(players)
# finds the players that has the most dropped passes
# 
# Params: 
#    players dict : contains the data on the players
# Returns: 
#    returns a list within a list, inside list has name and number of dropped passes
#    [[playername,yardslost],[playername,yardslost]]
def MostDroppedPasses(players):
    mostDropped=[]
    numDropped=0
    for player in players:
        if(players[player]['droppedpass']>numDropped):
            numDropped=players[player]['droppedpass']
            mostDropped=[[players[player]['name'],players[player]['droppedpass']]]
        elif(players[player]['droppedpass']==numDropped):
            mostDropped.append([players[player]['name'],players[player]['droppedpass']])
    return mostDropped  


f=open('PlayerInfo.json','r') 
players=json.load(f)
f.close()
f=open('TeamInfo.json','r')    
teams=json.load(f)
f.close()
f=open('FieldGoals.json','r')
fieldgoals=json.load(f)
f.close()
penaltieteams=[]

answer="Name: Sarah Beaver\nAssignment:A03 - Nfl Stats\nDate:2/11/2019\n\n"
answer+="==================================================================================\n"  
answer+="1. Find the player(s) that played for the most teams.\n\nAnswer:\n\n"
questionanswer= PlayersMostTeams(players)
for player in questionanswer:
    answer+=str(player[0]) +" played for "+str(player[1])+" teams.\n"

answer+="\n==================================================================================\n"
answer+="2. Find the player(s) that played for multiple teams in one year.\n\nAnswer:\n\n"
count=0
questionanswer=MultipleTeams(players)
# prints only top ten players for most teams, starting with one on most team then alphabeitacal order
for numteams in sorted(questionanswer.items(),reverse=True):
    for player in sorted(numteams[1].items()):
        count+=1
        answer+=player[0]+" played on " +str(numteams[0]) +" teams in the year " +player[1]+".\n"
        if(count==10):
            break
    if(count==10):
            break

answer+="\n==================================================================================\n"
answer+="3. Find the player(s) that had the most yards rushed for a loss.\n\nAnswer:\n\n"
questionanswer=RushedYardsLost(players)
for player in questionanswer:
    answer+=player[0]+" has lost "+str(player[1])+" yards while rushing.\n"

answer+="\n==================================================================================\n"
answer+="4. Find the player(s) that had the most rushes for a loss.\n\nAnswer:\n\n"
questionanswer=NumberRushesLost(players)
for player in questionanswer:
    answer+=player[0]+" rushed for a loss "+str(player[1])+" times.\n"

answer+="\n==================================================================================\n"
answer+="5. Find the player(s) with the most number of passes for a loss.\n\nAnswer:\n\n"
questionanswer=NumberPassesLost(players)
for player in questionanswer:
    answer+=player[0]+" passed for a loss "+str(player[1])+" times.\n"

answer+="\n==================================================================================\n"
answer+="6. Find the team with the most penalties.\n\nAnswer:\n\n"
questionanswer=TeamMostPenalties(teams)
for team in questionanswer:
    penaltieteams.append(team[0])
    answer+=team[0]+" had "+str(team[1])+" penalties.\n"

answer+="\n==================================================================================\n"
answer+="7. Find the team with the most yards in penalties.\n\nAnswer:\n\n"
questionanswer=TeamPenaltiesYards(teams)
for team in questionanswer:
    answer+=team[0]+" had "+str(team[1])+" yards lost to penalties.\n"

answer+="\n==================================================================================\n"
answer+="8. Find the team with the most yards in penalties.\n\nAnswer:\n\n"
questionanswer=PenaltyCorrelation(penaltieteams,teams)
answer+="Least Penalties: "+questionanswer[1][0]+" Wins: "+str(questionanswer[1][1])+"\n"
answer+="Most Penalties: "+questionanswer[0][0]+" Wins:"+str(questionanswer[0][1])+"\n"

answer+="\n==================================================================================\n"
answer+="9. Average number of plays in a game.\n\nAnswer:\n\n"
questionanswer=AveragePlays()
answer+=str(round(questionanswer))+" is the average number of plays in a game\n"

answer+="\n==================================================================================\n"
answer+="10. Longest field goal.\n\nAnswer:\n\n"
questionanswer=LongestFieldGoal(fieldgoals)
for player in questionanswer:
    answer+=player[0]+" has the longest made field goal at "+str(player[1])+" yards.\n"

answer+="\n==================================================================================\n"
answer+="11. Most field goals.\n\nAnswer:\n\n"
questionanswer=MostMadeFieldGoal(fieldgoals)
for player in questionanswer:
    answer+=player[0]+" has made the most field goals with "+str(player[1])+" made field goals.\n"

answer+="\n==================================================================================\n"
answer+="12. Most missed field goals.\n\nAnswer:\n\n"
questionanswer=MostMissedFieldGoal(fieldgoals)
for player in questionanswer:
    answer+=player[0]+" has missed the most field goals with "+str(player[1])+" missed field goals.\n"

answer+="\n==================================================================================\n"
answer+="13. Most dropped passes.\n\nAnswer:\n\n"
questionanswer=MostDroppedPasses(players)
for player in questionanswer:
    answer+=player[0]+" has dropped  "+str(player[1])+" passes.\n"

f=open("answer.txt",'w')
f.write(answer)
f.close()

# pprint(players)