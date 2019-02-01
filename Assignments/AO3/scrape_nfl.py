from beautifulscraper import BeautifulScraper
from pprint import pprint
import urllib
from urllib.request import urlretrieve
from time import sleep
import json

scraper = BeautifulScraper()
years =[x for x in range(2009,2019)]
weeks = [x for x in range(1,17)]

stype="REG"

gameids = {}
gameids["REG"]={}
gameids["POST"]={}
for year in years:
        print(year)
        gameids["REG"][year]={}
        for week in weeks:
                gameids["REG"][year][week]=[]
                url="http://www.nfl.com/schedules/%d/%s%d" %(year,stype,week)
                page = scraper.go(url)
                divs = page.find_all('div',{"class":"schedules-list-content"})
               
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

        for div in divs:
                gameids["POST"][year].append(div['data-gameid'])  
                try:
                        url="http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json"%(div['data-gameid'],div['data-gameid'])
                        urllib.request.urlretrieve(url, 'data/'+div['data-gameid']+'.json')  
                except: 
                        print("Page not found for "+div['data-gameid'])     
pprint(gameids)
f=open("GameIds.json",'w')
f.write(json.dumps(gameids))
f.close()
