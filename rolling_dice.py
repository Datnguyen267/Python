"""
- The Goal: Rolling number in a specific range
- Author: Dat Nguyen
- Create date: 2018-02-09
"""

import random
def rolling_dice():
  while True:
    ask_user = input("Do you want to roll dice?(Y/N) ")
    if ask_user.lower() == "y":
      print(random.randint(1, 6))
    else :
      break

rolling_dice()
