"""
Course: cmps 4883
Assignemt: A03
Date: 2/04/19
Github username: bluefire8421
Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
Name: Sarah Beaver
Description: 
    gets all the game ids from 2009 to now and the scraps the game data from nfl
"""
from beautifulscraper import BeautifulScraper
from pprint import pprint
import urllib
from urllib.request import urlretrieve
from time import sleep
import json

scraper = BeautifulScraper()
years =[x for x in range(2009,2019)]
weeks = [x for x in range(1,18)]

stype="REG"

gameids = {}
gameids["REG"]={}
gameids["POST"]={}
for year in years:
        # getting every year in 2009 to 2019
        print(year)
        gameids["REG"][year]={}
        # getting every week in the regular season
        for week in weeks:
                gameids["REG"][year][week]=[]
                url="http://www.nfl.com/schedules/%d/%s%d" %(year,stype,week)
                page = scraper.go(url)
                divs = page.find_all('div',{"class":"schedules-list-content"})
                # adds the game id to the json then pulls the liveupdate stats of that game
                for div in divs:
                        gameids["REG"][year][week].append(div['data-gameid'])
                        try:
                                url="http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json"%(div['data-gameid'],div['data-gameid'])
                                urllib.request.urlretrieve(url, 'data/'+div['data-gameid']+'.json') 
                        except: 
                                print("Page not found for "+div['data-gameid'])                        

        gameids["POST"][year]=[]
        url="http://www.nfl.com/schedules/%d/%s" %(year,"POST")
        page = scraper.go(url)
        divs = page.find_all('div',{"class":"schedules-list-content"})
        # add the gameid from the post season, add gameid to json and pulls the stats
        for div in divs:
                gameids["POST"][year].append(div['data-gameid'])  
                try:
                        url="http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json"%(div['data-gameid'],div['data-gameid'])
                        urllib.request.urlretrieve(url, 'data/'+div['data-gameid']+'.json')  
                except: 
                        print("Page not found for "+div['data-gameid'])     
# dumping all game ids into a json
f=open("GameIds.json",'w')
f.write(json.dumps(gameids))
f.close()
