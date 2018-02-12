"""
- The Goal: Check user's input is prime or not.
- Author: Dat Nguyen
- Create date: 2018-02-12
"""

import random
def is_prime(number = 2):
  result = True
  if number < 2:
    result = False
  else:
    for i in range(2, number):
      if number % i == 0:
        result = False
  return result

print("Let's check your number")
while True:
  number = int(input("Enter a number: "))
  
  if is_prime(number) == True:
    print("Number %s is prime." % (number))
  else:
    print("Number %s is not prime." % (number))
  ask_for_cont = input("Do you want to continue?(Y/N) ")
  if ask_for_cont.upper() != "Y":
    break
