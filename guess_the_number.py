"""
- The Goal: Try to guess a number in three times, you will know lastest guess is exact, hight or low.
- Author: Dat Nguyen
- Create date: 2018-02-09
"""

import random
def guess_the_number():
  secret_number = random.randint(1, 100)
  memo_dict = {
    0: "first",
    1: "second",
    2: "third"
    }
  for i in range(3):
    ask_user = int(input("Guess a number baby: "))
    print("Your %s guess %s" %(memo_dict[i], str(ask_user)))
    if ask_user == secret_number:
      print("Congratulation!!! %s is sercet number." %(str(secret_number)))
      break
    elif ask_user < secret_number:
      print("Try again baby. %s is lower than secret number." %(str(ask_user)))
    else : #ask_user > secret_number
      print("Try again baby. %s is higher than secret number." %(str(ask_user)))
    if i == 2:
      print("You lose, try again later")

print("Let's play")
while True:
  guess_the_number()
  ask_for_cont = input("Do you want to continue?(Y/N) ")
  if ask_for_cont.upper() != "Y":
    break
