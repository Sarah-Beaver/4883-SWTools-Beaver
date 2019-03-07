"""
Course: cmps 4883
Assignemt: A03
Date: 3/05/19
Github username: bluefire8421
Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
Name: Sarah Beaver
Description: 
    scraping emojis from the url to use later in an image, they are saved in a emojis folder
"""
from pprint import pprint
from bs4 import BeautifulSoup
import requests

url = "https://www.webfx.com/tools/emoji-cheat-sheet/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# loops through each emoji on the webpage and request to specific url for the emoji
for emoji in soup.find_all("span",{"class":"emoji"}):
    image_path = emoji['data-src']
    response = requests.get(url+image_path, stream=True)
    text=image_path.split("/")
    # if the response is good then it opens the emojis folder and writes the emoji to personel file
    if response.status_code == 200:
        with open("./emojis/"+text[2], 'wb') as f:
            f.write(response.content)
            f.close()
    else:
        print("couldn't load "+text[2])