import wget
import json
import os.path

if not os.path.exists('gfnpc.json') :
    fs = wget.download(url='https://static.nvidiagrid.net/supported-public-game-list/gfnpc.json')
else :
    with open('gfnpc.json', encoding="utf8") as f :
        games_list = f.read()
        games = json.loads(games_list)
    for game in games :
        steamUrl = game['steamUrl']
        if steamUrl != "" :
            gameID = steamUrl.replace("https://store.steampowered.com/app/", "")
            fs = wget.download(url='https://store.steampowered.com/api/appdetails?appids='+gameID, out="json/"+gameID+".json")
            with open("json/"+gameID+".json", encoding="utf8") as f:
                steam = f.read()
                steamGame = json.loads(steam)
            print("Downloading " + game['title'])
            wget.download(steamGame[gameID]['data']['header_image'], 'images/'+game['title']+".jpg")
