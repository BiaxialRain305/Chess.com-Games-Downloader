from datetime import datetime, timedelta
from chessdotcom import client
import json
import os
import datetime
    
# Gets all the games played
def all_games(username):
    folder_name = f"{username} - Games"
    timestamp = client.get_player_profile(username).player.joined
    joined_datetime = datetime.datetime.fromtimestamp(timestamp)
    current_datetime = datetime.datetime.now()
    elapsed_time = current_datetime - joined_datetime
    num_months = elapsed_time.days // 30
    inp = input("NOTE: Chess.com allows you to import more than one PGN however lichess doesn't as far as I know\n\nWould you like each game in a seperate pgn file? (y/n): ")
    while inp.lower() not in ["y", "n"]:
        inp = input("Invalid Input\nWould you like each game in a seperate pgn file? (y/n): ").lower()
    

    if inp.lower() == "y":
        os.mkdir(folder_name)
        
    # Read list
    for i in range(num_months+1):
        month = (joined_datetime + timedelta(days=30*i)).strftime("%m")
        year = (joined_datetime + timedelta(days=30*i)).strftime("%Y")
        
        
        games_str = client.get_player_games_by_month_pgn(username, year, month).json["pgn"]["pgn"]
        lines = games_str.split('\n\n')
        result = []
        current_line = ""
        for i, line in enumerate(lines):
            current_line += line
            if (i+1) % 2 == 0:  # even line number (including 0)
                result.append(current_line)
                current_line = ""
        
        if current_line:
            result.append(current_line)
    if inp.lower() == "n":
        file_name = os.path.join(folder_name, "All_Games.pgn")
        f = open(file_name, "w")
        f.write("\n".join(result))
        f.close()
    else:
        for count, i in enumerate(result):
            file_name = os.path.join(folder_name, f"Game{count}.pgn")
            file = open(file_name, "w")
            file.write(i)
            file.close()
            
            
    

if __name__ == "__main__":
    username = input("Enter a chess.com username: ")
    all_games(username)
    print("DONE")
