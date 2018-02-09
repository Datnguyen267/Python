"""
- The Goal: Check list less than ...
- Author: Dat Nguyen
- Create date: 2018-02-09
"""

import random
def list_less_than(number):
  list = [random.randint(1, 100) for i in range(20)]
  result = [x for x in list if x < number]
  return result

number = int(input("Input a number: "))
print(list_less_than(number))
