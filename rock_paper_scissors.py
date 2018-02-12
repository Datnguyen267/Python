"""
- The Goal: Rock Paper Scissors game.
- Author: Dat Nguyen
- Create date: 2018-02-12
"""

import random
def rock_paper_scissors(player_1, player_2):
  result = ""
  if (player_1 == "R" and player_2 == "S") or \
     (player_1 == "S" and player_2 == "P") or \
     (player_1 == "P" and player_2 == "R"):
    result = "Player_1 win."
  elif (player_2 == "R" and player_1 == "S") or \
     (player_2 == "S" and player_1 == "P") or \
     (player_2 == "P" and player_1 == "R"):
    result = "Player_2 win."
  else:
    result = "Draw!"
  return result


print("Let's play")
short_list = ["R", "P", "S"]
full_dict = {
  "R": "Rock",
  "P": "Paper",
  "S": "Scissors"
  }
while True:
  player_1 = input("Rock(R) paper(P) scissors(S)? ")
  player_2 = input("Rock(R) paper(P) scissors(S)? ")
  if (player_1.upper() not in short_list) or \
     (player_2.upper() not in short_list):
    print("Oh, something wrong. You only choose Rock(R) paper(P) scissors(S).\
          \nLet's try again")
    continue
  else:
    print("Player_1 chosen %s.\nPlayer_2 chosen %s." \
          %(full_list[player_1.upper()], full_list[player_2.upper()]))
    print(rock_paper_scissors(player_1.upper(), player_2.upper()))
  ask_for_new_game = input("Do you want to start a new game?(Y/N) ")
  if ask_for_new_game.upper() != "Y":
    break
