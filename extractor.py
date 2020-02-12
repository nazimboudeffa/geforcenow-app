import wget
import json
import os.path
import requests
import urllib.request

#if not os.path.exists('gfnpc.json'): fs = wget.download(url='https://static.nvidiagrid.net/supported-public-game-list/gfnpc.json')

with open('gfnpc.json', encoding="utf8") as f:
    games_list = f.read()
    games = json.loads(games_list)
#r = requests.get(url='https://static.nvidiagrid.net/supported-public-game-list/gfnpc.json')
#games = json.dumps(r.json())

for game in games:
    steamUrl = game['steamUrl']
    if steamUrl != "" :
        gameID = steamUrl.replace("https://store.steampowered.com/app/", "")
        #r = requests.get(url='https://store.steampowered.com/api/appdetails?appids='+gameID)
        fs = wget.download(url='https://store.steampowered.com/api/appdetails?appids='+gameID, out="json/"+gameID+".json")
        #steamGame = json.dumps(r.json())
        with open("json/"+gameID+".json", encoding="utf8") as f:
            steam = f.read()
            steamGame = json.loads(steam)
        print("Downloading " + game['title'])
        #urllib.request.urlretrieve(steamGame[gameID]['data']['header_image'], 'images/'+game['title']+".jpg")
        wget.download(steamGame[gameID]['data']['header_image'], 'images/'+game['title']+".jpg")
