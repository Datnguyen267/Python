"""
- The Goal: Get max number of three without max function
- Author: Dat Nguyen
- Create date: 2018-02-13
"""

import random
def max_of_three(number_1, number_2, number_3):
  result = number_1
  if number_2 > result:
    result = number_2
  if number_3 > result:
    result = number_3
  return result

number_1 = random.randint(0, 100)
number_2 = random.randint(0, 100)
number_3 = random.randint(0, 100)
number_max = max_of_three(number_1, number_2, number_3)
print("Max of %s, %s, %s is %s" %(number_1, number_2, number_3, number_max))
  
