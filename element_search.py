"""
- The Goal: Element search using Binary search 
- Author: Dat Nguyen
- Create date: 2018-02-12
"""

import random

def binary_search(number):
  temp_list = list_search
  temp_number = 0
  result = False
  while len(temp_list) > 1:
    temp_number = temp_list[int(len(temp_list) / 2)]
    if temp_number == number:
      result = True
      break
    elif temp_number > number:
      temp_list = temp_list[0 : int(len(temp_list) / 2): 1]
    else:
      temp_list = temp_list[int(len(temp_list) / 2 ): len(temp_list) : 1] 
    
  return result

list_search = random.sample(range(40), 20)
list_search.sort()
number = int(input("Enter number to search: "))
print(binary_search(number))



