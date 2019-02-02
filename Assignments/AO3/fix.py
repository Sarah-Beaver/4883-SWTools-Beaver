import urllib
from urllib.request import urlretrieve
from time import sleep
import json
# these two files came back as not json so regetting the data
# Is not json 2009112901.json
# Is not json 2009092005.json

url="http://www.nfl.com/liveupdate/game-center/2009112901/2009112901_gtd.json"
urllib.request.urlretrieve(url, 'data/'+'2009112901.json')

url="http://www.nfl.com/liveupdate/game-center/2009092005/2009092005_gtd.json"
urllib.request.urlretrieve(url, 'data/'+'2009092005.json')