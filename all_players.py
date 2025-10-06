import pandas as pd
from roster import scrape_roster
import json
import time


'''
Uses team_ids.json to get team ids that we use to scrape the roster of
Makes a dictionary where each player_id is associated with their team. 
Will be exported into another json that can then be used to scrape the player infos

'''
def get_all_players() -> None:
    with open("team_ids.json", "r") as f:
        ids = json.load(f)
    all_players : dict[int:int] = {}
    for team_id in ids:
        print(team_id)
        try:
            roster = list(scrape_roster(int(team_id))["Player_id"])
        except:
            with open("players.json", "w") as f:
                json.dump(all_players, f, indent=4)
            return

        for player in roster:
            all_players[int(player)] = team_id
        time.sleep(3)

    with open("players.json", "w") as f:
        json.dump(all_players, f, indent=4)



if __name__ == '__main__':
    # get_all_players()
    with open("players.json", "r") as f:
        data = json.load(f)
    int_dict = {int(k): v for k, v in data.items()}
    with open("players2.json", "w") as f:
        json.dump(int_dict, f, indent=4)
