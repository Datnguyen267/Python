"""
- The Goal: Try to guess a number in three times, you will know lastest guess is exact, hight or low.
- Author: Dat Nguyen
- Create date: 2018-02-09
"""

import random
def guess_the_number():
  secret_number = random.randint(1, 100)
  for i in range(3):
    ask_user = int(input("Guess a number baby: "))
    print("You guess %s" %(str(ask_user)))
    if ask_user == secret_number:
      print("Congratulation!!! %s is sercet number." %(str(secret_number)))
      break
    elif ask_user < secret_number:
      print("Try again baby. %s is lower than secret number." %(str(ask_user)))
    else : #ask_user > secret_number
      print("Try again baby. %s is higher than secret number." %(str(ask_user)))

guess_the_number()
