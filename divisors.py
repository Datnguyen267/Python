"""
- The Goal: Get all divisors of a number
- Author: Dat Nguyen
- Create date: 2018-02-09
"""

import random
def get_all_divisors(number):
  result = [x for x in range(1, number) if number % x == 0]
  return result

number = int(input("Input a number: "))
print(get_all_divisors(number))
