"""
- The Goal: Take all even elements in a list.
- Author: Dat Nguyen
- Create date: 2018-02-12
"""

import random
def list_comprehensions(numbers):
  result = [x for x in numbers if x % 2 == 0]
  return result

numbers = random.sample(range(100), 20)
print(list_comprehensions(numbers))
