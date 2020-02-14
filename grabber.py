import wget
import json
import os.path

steamCount = 0

if not os.path.exists('public/gfnpc.json') :
    fs = wget.download(url='https://static.nvidiagrid.net/supported-public-game-list/gfnpc.json', out='public/gfnpc.json')
    with open('public/gfnpc.json', encoding="utf8") as f :
        games_list = f.read()
        games = json.loads(games_list)
else :
    with open('public/gfnpc.json', encoding="utf8") as f :
        games_list = f.read()
        games = json.loads(games_list)

for game in games :
    steamUrl = game['steamUrl']
    if steamUrl != "" :
        steamCount += 1
        gameID = steamUrl.replace("https://store.steampowered.com/app/", "")
        if not os.path.exists("public/json/"+gameID+".json") :
            fs = wget.download(url='https://store.steampowered.com/api/appdetails?appids='+gameID, out="public/json/"+gameID+".json")
            with open("public/json/"+gameID+".json", encoding="utf8") as f:
                steam = f.read()
                steamGame = json.loads(steam)
        else :
            with open("public/json/"+gameID+".json", encoding="utf8") as f:
                steam = f.read()
                steamGame = json.loads(steam)
        if not os.path.exists('public/images/'+gameID+".jpg") :
            print("Downloading " + gameID + " " + game['title'])
            if (steamGame[gameID]['success']== True) :
                wget.download(url=steamGame[gameID]['data']['header_image'], out='public/images/'+gameID+".jpg")
            else :
                print(gameID + " " + game['title'] + "Doesn't exist ... Please contact GForceNow on the forum")
        else :
            print("Already have "  + gameID + " " + game['title'])
        print(str(steamCount) + " Steam games")
