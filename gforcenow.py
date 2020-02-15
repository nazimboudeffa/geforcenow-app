import wget
import json
import os
import sys


header = "\
  ___________________                           _______                  \n\
 /  _____/\_   _____/__________   ____  ____    \      \   ______  _  __ \n\
/   \  ___ |    __)/  _ \_  __ \_/ ___\/ __ \   /   |   \ /  _ \ \/ \/ / \n\
\    \_\  \|     \(  <_> )  | \/\  \__\  ___/  /    |    (  <_> )     /  \n\
 \______  /\___  / \____/|__|    \___  >___  > \____|__  /\____/ \/\_/   \n\
        \/     \/                    \/    \/          \/                \n"

def menu():
    print (header)
    print ("version 0.1")

    choice = input("""
                      A: Grab An Image
                      B: Grab All Images
                      C: Sync with GForce
                      Q: Quit/Log Out

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        todo()
    elif choice == "B" or choice =="b":
        grabAll()
    elif choice == "C" or choice =="c":
        synch()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or Q.")
        print("Please try again")
        menu()

def todo():
    print("todo")

def grabAll():
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

menu()
