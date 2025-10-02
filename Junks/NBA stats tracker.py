from nba_api.stats.endpoints import PlayerGameLog
from nba.api.stats.endpoints import Players
from tabulate import tabulate
import pandas as pd

def search_player(name):
 player = players.find_players_by_full_name(name)
 if not player:
  return "Player not found"
 return player[0]

def get_stats(player_id):
 gamelog = PlayerGameLog(player_id=player_id, season='2024-2025')
 df = gamelog.get_data_frame()[0]

 df_selected = df[['GAME_DATE','MATCHUP','PTS','REB','AST','MINS']] 
 df_selected.columns =['Date','Matchup','Points','Rebounds','Assist','Minutes']

 return df_selected


def main():
 name = input ("Enter Player: ")
 player = search_player(name)

 if isinstance(player,str):
   print(player)
   return

try:
  stats = get_stats(player['id'])
  print(f"\nStatistics for {player['full_name']} (Season 2024-25):")
  print(tabulate(stats,headers='Keys', tablefmt='grid', showindex=false))

except Exception as e:
 print(f"Error: {e}" )

if __name__ == "__main__":
 main()
