"""
- The Goal: Cows And Bulls game
- Author: Dat Nguyen
- Create date: 2018-02-12
"""

import random

def cows_and_bulls(guess = 0000):
  temp_guess = [int(x) for x in guess]
  cows = bulls = 0
  for i in range(4):
    if temp_guess[i] == secret[i]:
      cows += 1
  for i_g, v_g in enumerate(temp_guess):
    for i_s, v_s in enumerate(secret):
      if (v_g == v_s) and (i_g != i_s):
        bulls += 1

  return {'cows': cows, 'bulls': bulls}

secret = random.sample(range(9), 4)
count_guess = 0
print("Let's play!")
while True:
  guess = input("Guess a 4-digit number: ")
  result = cows_and_bulls(guess)
  print("%s cows, %s bulls" %(str(result['cows']), str(result['bulls'])))
  count_guess += 1
  if result['cows'] == 4:
    print("Congratulation, %s is secret number." %(guess))
    break
  else:
    print("Try again!")
print("You spend %s times to guess exactly." %(count_guess))
  



