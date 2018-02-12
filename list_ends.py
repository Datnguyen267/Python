"""
- The Goal: Get first and last element in a list.
- Author: Dat Nguyen
- Create date: 2018-02-12
"""

import random
def list_ends(numbers = []):
  result = []
  result.append(numbers[0])
  result.append(numbers[len(numbers) - 1])
  return result

numbers = random.sample(range(100), 10)

print(list_ends(numbers))
