import wget
import json
import os.path

steamCount = 0

if not os.path.exists('gfnpc.json') :
    fs = wget.download(url='https://static.nvidiagrid.net/supported-public-game-list/gfnpc.json')
    with open('gfnpc.json', encoding="utf8") as f :
        games_list = f.read()
        games = json.loads(games_list)
else :
    with open('gfnpc.json', encoding="utf8") as f :
        games_list = f.read()
        games = json.loads(games_list)

for game in games :
    steamUrl = game['steamUrl']
    if steamUrl != "" :
        steamCount += 1
        gameID = steamUrl.replace("https://store.steampowered.com/app/", "")
        if not os.path.exists("json/"+gameID+".json") :
            fs = wget.download(url='https://store.steampowered.com/api/appdetails?appids='+gameID, out="json/"+gameID+".json")
            with open("json/"+gameID+".json", encoding="utf8") as f:
                steam = f.read()
                steamGame = json.loads(steam)
        else :
            with open("json/"+gameID+".json", encoding="utf8") as f:
                steam = f.read()
                steamGame = json.loads(steam)
        if not os.path.exists('images/'+gameID+".jpg") :
            print("Downloading " + gameID + " " + game['title'])
            if (steamGame[gameID]['success']== True) :
                wget.download(url=steamGame[gameID]['data']['header_image'], out='images/'+gameID+".jpg")
            else :
                print(gameID + " " + game['title'] + "Doesn't exist ... Please contact GForceNow on the forum")
        else :
            print("Already have "  + gameID + " " + game['title'])

print("You have " + steamCount + " Steam games")
