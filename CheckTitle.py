#!/usr/bin/env python3

from PIL import Image
from io import BytesIO
import requests
import sys
import os

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def checkTitle(tid):
    if(tid.startswith("00050000-")):
        return True
    else:
        return False
    return False

print("################################################")
print("          WiiU CheckTitle - By VCoding          ")
print("################################################")
print("\n")

print('Enter the TitleID to be checked using the following format: "00050000-10176A00".')
print(f'{color.WARNING}WARNING: This only works with TitleIDs starting with "00050000".{color.ENDC}')
tid=input(f"{color.HEADER}>> ")
print(color.ENDC)

if len(tid) != 17:
    print(f"{color.FAIL}ERROR: Your entry must be 17 characters long!")
    sys.exit()

if not checkTitle(tid):
    print(f"{color.FAIL}ERROR: The TitleID you entered is not valid!")
    sys.exit()

rq = requests.get("https://cemui.com/api/v2/GetGame/title_id/" + tid)
if (rq.status_code != 200):
    print(f"{color.FAIL}ERROR: An error occurred when sending the request.")
    sys.exit()

rJSON = rq.json()

if("error" in rJSON):
    print(f"{color.FAIL}ERROR: Your TitleID is wrong or does not exist!")
    sys.exit()

print(f'{color.OKGREEN}SUCCESS: The titleID exists!')
print(color.ENDC)
print("Here is the menu, you can enter a number to get information about the game.")
print("1. Display all the information about the game")
print("2. Display basic game information")
print("3. View technical information about the game")
print("4. Display the game cover")
print("5. Display the game icon")
print("6. Displays a screenshot of the game")
print("7. Display the grid of the game")
print("8. Display the Json")
print("9. Display the menu again")
print("10. Exit")

while(1):
    rep = input(f"{color.HEADER}>> ")
    if(rep == "1"):
        print(color.ENDC + color.BOLD + "Game name: " + color.ENDC + rJSON["game_title"])
        if(rJSON['game_overview'] == None):
            print(color.BOLD + "Description: " + color.ENDC + "None")
        else:
            print(color.BOLD + "Description: " + color.ENDC + rJSON['game_overview'])
        print(color.BOLD + "TitleID: " + color.ENDC + rJSON["game_title_id"])
        print(color.BOLD + "Product Code: " + color.ENDC + rJSON["game_product_code"])
        if(rJSON['game_developer'] == None):
            print(color.BOLD + "Game Developer: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Game Developer: " + color.ENDC + rJSON['game_developer'])
        if(rJSON['game_publisher'] == None):
            print(color.BOLD + "Game Publisher: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Game Publisher: " + color.ENDC + rJSON['game_publisher'])
        if(rJSON['game_title_id'] == "00050000-10105700"):
            print(color.BOLD + "Game Region: " + color.ENDC + "All")
        if(rJSON['game_region'] == None and rJSON['game_title_id'] == "00050000-10105700"):
            print(color.BOLD + "Game Region: " + color.ENDC + "Unknown")
        elif not rJSON['game_title_id'] == "00050000-10105700":
            print(color.BOLD + "Game Region: " + color.ENDC + rJSON['game_region'])
        if(rJSON['game_release_region'] == None):
            print(color.BOLD + "Game Release Region: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Game Release Region: " + color.ENDC + rJSON['game_release_region'])
        if(rJSON['game_version'] == None):
            print(color.BOLD + "Game Version: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Game Version: " + color.ENDC + rJSON['game_version'])
        if(rJSON['game_esrb'] == None):
            print(color.BOLD + "ESRB: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "ESRB: " + color.ENDC + rJSON['game_esrb'])
        if(rJSON['game_max_players'] == None):
            print(color.BOLD + "Max Players: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Max Players: " + color.ENDC + rJSON['game_max_players'])
        if(rJSON['game_release_date'] == None):
            print(color.BOLD + "Release Date: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Release Date: " + color.ENDC + rJSON['game_release_date'])
        if(rJSON['game_coop'] == None):
            print(color.BOLD + "Cooperation: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Cooperation: " + color.ENDC + rJSON['game_coop'])
        if(rJSON['game_genres'] == None):
            print(color.BOLD + "Genres: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Genres: " + color.ENDC + rJSON['game_genres'])
        if(rJSON['game_eshop_id'] == None):
            print(color.BOLD + "eShop ID: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "eShop ID: " + color.ENDC + rJSON['game_eshop_id'])
        print(color.BOLD + "Game ID: " + color.ENDC + rJSON["game_id"])
        if(rJSON['game_slug'] == None):
            print(color.BOLD + "Game Slug: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Game Slug: " + color.ENDC + rJSON["game_slug"])
    if(rep == "2"):
        print(color.ENDC + color.BOLD + "Game name: " + color.ENDC + rJSON["game_title"])
        if(rJSON['game_overview'] == None):
            print(color.BOLD + "Description: " + color.ENDC + "None")
        else:
            print(color.BOLD + "Description: " + color.ENDC + rJSON['game_overview'])
        print(color.BOLD + "TitleID: " + color.ENDC + rJSON["game_title_id"])
        if(rJSON['game_release_date'] == None):
            print(color.BOLD + "Release Date: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Release Date: " + color.ENDC + rJSON['game_release_date'])
        if(rJSON['game_title_id'] == "00050000-10105700"):
            print(color.BOLD + "Game Region: " + color.ENDC + "All")
        if(rJSON['game_region'] == None and rJSON['game_title_id'] == "00050000-10105700"):
            print(color.BOLD + "Game Region: " + color.ENDC + "Unknown")
        elif not rJSON['game_title_id'] == "00050000-10105700":
            print(color.BOLD + "Game Region: " + color.ENDC + rJSON['game_region'])
        if(rJSON['game_esrb'] == None):
            print(color.BOLD + "ESRB: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "ESRB: " + color.ENDC + rJSON['game_esrb'])
    if(rep == "3"):
        print(color.ENDC + color.BOLD + "Product Code: " + color.ENDC + rJSON["game_product_code"])
        if(rJSON['game_eshop_id'] == None):
            print(color.BOLD + "eShop ID: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "eShop ID: " + color.ENDC + rJSON['game_eshop_id'])
        print(color.BOLD + "Game ID: " + color.ENDC + rJSON["game_id"])
        if(rJSON['game_slug'] == None):
            print(color.BOLD + "Game Slug: " + color.ENDC + "Unknown")
        else:
            print(color.BOLD + "Game Slug: " + color.ENDC + rJSON["game_slug"])
        
    if(rep == "4"):
        if not rJSON['game_boxart_url'] == None:
            print(f"{color.WARNING}WARNING: That action's gonna take a while. Please hold...")
            screenshot = requests.get(rJSON["game_boxart_url"])
            if(screenshot.status_code != 200):
                print(f"{color.FAIL}ERROR: An error has occurred.")
            else:
                img = Image.open(BytesIO(screenshot.content))
                img.show()
                print(f"{color.OKGREEN}The operation was a success!")
        else:
            print(f"{color.FAIL}No image of the box is available!")
    if(rep == "5"):
        if not rJSON['game_icon_url'] == None:
            print(f"{color.WARNING}WARNING: That action's gonna take a while. Please hold...")
            screenshot = requests.get(rJSON["game_icon_url"])
            if(screenshot.status_code != 200):
                print(f"{color.FAIL}ERROR: An error has occurred.")
            else:
                img = Image.open(BytesIO(screenshot.content))
                img.show()
                print(f"{color.OKGREEN}The operation was a success!")
        else:
            print(f"{color.FAIL}No game icons are available!")
    if(rep == "6"):
        if not rJSON["game_screenshot_urls"] == None:
            if("|" in rJSON["game_screenshot_urls"]):
                print(f"{color.FAIL}ERROR: The game contains several screenshot.")
                print("Unfortunately, the software is not yet compatible.\n")
                print(rJSON["game_screenshot_urls"].replace("|", "\n"))
            else:
                print(f"{color.WARNING}WARNING: That action's gonna take a while. Please hold...")
                screenshot = requests.get(rJSON["game_screenshot_urls"])
                if(screenshot.status_code != 200):
                    print(f"{color.FAIL}ERROR: An error has occurred.")
                else:
                    img = Image.open(BytesIO(screenshot.content))
                    img.show()
                    print(f"{color.OKGREEN}The operation was a success!")
        else:
            print(f"{color.FAIL}No screenshot is available for this application / game!")
    if(rep == "7"):
        if not rJSON['game_grid_image_url'] == None:
            print(f"{color.WARNING}WARNING: That action's gonna take a while. Please hold...")
            screenshot = requests.get(rJSON["game_grid_image_url"])
            if(screenshot.status_code != 200):
                print(f"{color.FAIL}ERROR: An error has occurred.")
            else:
                img = Image.open(BytesIO(screenshot.content))
                img.show()
                print(f"{color.OKGREEN}The operation was a success!")
        else:
            print(f"{color.FAIL}No grid of the game is available!")
    if(rep == "8"):
        print(rJSON)
    if(rep == "9"):
        print(color.ENDC + "Here is the menu, you can enter a number to get information about the game.")
        print("1. Display all the information about the game")
        print("2. Display basic game information")
        print("3. View technical information about the game")
        print("4. Display the game cover")
        print("5. Display the game icon")
        print("6. Displays a screenshot of the game")
        print("7. Display the grid of the game")
        print("8. Display the Json")
        print("9. Display the menu again")
        print("10. Exit")
    if(rep == "10" or rep == "exit" or rep == "exit()" or rep == "close"):
        break
