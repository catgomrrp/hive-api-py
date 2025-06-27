from datetime import datetime
import json
import requests
import time

base_url = "https://api.playhive.com/v0/"


def make_request(url):
    print("Making a response to " + url + "...")
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        print("Error: " + str(response))
        return None

def main_menu():
    print("Main Menu:")
    print("1. Player Info")
    print("2. Leaderboards")
    print("3. Miscellaneous")
    print("4. Dump Catalogue / Leaderboard")

    user_input = int(input())

    if user_input == 1:
        player_info()
    
    elif user_input == 2:
        leaderboards()

    elif user_input == 3:
        misc()

    elif user_input == 4:
        dump()

    else:
        print("Enter a number for an option")
        main_menu()

def player_info():
    print("Player Info:")
    print("1) Player Search")

    user_input = int(input())

    if user_input == 1:
        search = input("Enter your player search prefix (4+ characters): ")
        url = base_url + "player/search/" + search
        search_results = make_request(url)
        print(search_results.json())

    else:
        print("Enter a number for an option")
        player_info()

def leaderboards():
    print("Leaderboards:")

def misc():
    print("Miscellaneous Options:")
    print("1. Global Statistics")
    print("2. Costume Catalogue")
    print("3. Display Costume by ID")
    print("4. Hub Title Catalogue")
    print("5. Display Hub Title by ID")
    print("6. List Maps in a Game")
    print("7. List Metadata for a Game")

    user_input = int(input())

    if user_input == 1:
        url = base_url + "global/statistics"
        global_statistics = make_request(url)
        if global_statistics:
            print("Global Statistics:")
            print(global_statistics.json())

    elif user_input == 2:
        amount = input("Enter the amount of costumes to display (maximum of 50, default of 50): ")

        if amount == "":
            amount = "50"
        elif int(amount) > 50:
            print("Amount too high, setting to 50.")

        skip = input("Enter the amount of costumes to skip (default of 0): ")

        if skip == "":
            skip = "0"

        url = base_url + "catalogue/costumes?limit=" + amount + "&offset" + skip
        catalogue = make_request(url)
        if catalogue:
            print("Costume Catalogue:")
            print(catalogue.json())

    elif user_input == 3:
        costume_ID = input("Enter a Costume ID: ")
        url = base_url + "catalogue/costumes/" + costume_ID
        costume = make_request(url)
        if costume:
            print("Costume Details:")
            print(costume.json())

    elif user_input == 4:
        amount = input("Enter the amount of hub titles to display (maximum of 50, default of 50): ")

        if amount == "":
            amount = "50"
        elif int(amount) > 50:
            print("Amount too high, setting to 50.")

        skip = input("Enter the amount of hub titles to skip (default of 0): ")

        if skip == "":
            skip = "0"

        url = base_url + "catalogue/titles?limit=" + amount + "&offset" + skip
        catalogue = make_request(url)
        if catalogue:
            print("Title Catalogue:")
            print(catalogue.json())

    elif user_input == 5:
        title_ID = input("Enter a Hub Title ID: ")
        url = base_url + "catalogue/titles/" + title_ID
        title = make_request(url)
        if title:
            print("Hub Title Details:")
            print(title.json())

    elif user_input == 6:
        game = input("Enter a game to list maps for (ex: bed): ")
        url = base_url + "game/map/" + game
        maps = make_request(url)
        if maps:
            print("Maps in " + game + ":")
            print(maps.json())

    elif user_input == 7:
        game = input("Enter a game to list metadata for (ex: bed): ")
        url = base_url + "game/meta/" + game
        metadata = make_request(url)
        if metadata:
            print("Metadata for " + game + ":")
            print(metadata.json())

    else:
        print("Enter a number for an option")
        misc()

def dump():
    print("Dump Catalogue / Leaderboard")
    print("1. Catalogue (Costumes & Hub Titles)")
    print("2. Leaderboards")

    user_input = int(input())

    if user_input == 1:
        def dump_catalogue(catalogue):
            print("Starting " + catalogue + "...")
            catalogue_json = []
            amount = 50
            skip = 0
            url = base_url + "catalogue/" + str(catalogue) + "?limit=" + str(amount) + "&offset=" + str(skip)
        
            while True:
                catalogue_response = make_request(url)
            
                if not catalogue_response.json():
                    print("Finished, stopping.")
                    break

                catalogue_json.append(catalogue_response.json())
            
                skip = skip + 50
                url = base_url + "catalogue/" + str(catalogue) + "?limit=" + str(amount) + "&offset=" + str(skip)
            
                time.sleep(3)

            file_name = catalogue + "_" + datetime.today().strftime("%Y-%m-%d-%-H-%M-%S") + ".json"
            print("Writing to " + file_name)
            open(file_name, "wb").write(json.dumps(catalogue_json, indent=4).encode("UTF-8"))
        
        dump_catalogue("costumes")
        dump_catalogue("titles")

    elif user_input == 2:
        print("Starting...")
    
    else:
        print("Enter a number for an option")
        dump()

main_menu()