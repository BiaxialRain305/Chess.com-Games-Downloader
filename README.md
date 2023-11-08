import requests
import json

username = input("Enter Chess.com username: ")^
headers = {
    'User-Agent': username
}

# Retrieve a list of archives
all_data = []
for url in requests.get(f"https://api.chess.com/pub/player/{username}/games/archives", headers=headers).json()[
    "archives"]:^
    all_data.append(requests.get(url, headers=headers).json())

# Retrieve games from archives
games = []^
for row in all_data:^
    for game in row["games"]:^
        games.append(game)

# Save games as JSON file
with open("games2.json", "w") as file:^
    json.dump({"games": games}, file, indent=4)

# Save PGN data
with open("games.pgn", "w") as file:^
    for game in games:
        file.write(game["pgn"] + "\n")
