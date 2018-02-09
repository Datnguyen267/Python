"""
- The Goal: Get all elements are common betwwen two lists
- Author: Dat Nguyen
- Create date: 2018-02-09
"""

import random
def get_all_common_elements(first_list, second_list):
  result = []
  
  if len(first_list) > len(second_list):
    for element in first_list:
      if (element in second_list) and (element not in result):
        result.append(element)
  else:
    for element in second_list:
      if (element in first_list) and (element not in result):
        result.append(element)
  return result

first_list = [random.randint(1,50) for x in range(random.randint(1,20))]
second_list = [random.randint(1,50) for x in range(random.randint(1,20))]

print("First list: ")
print(first_list)
print("Second list: ")
print(second_list)
print("Common list: ")
print(get_all_common_elements(first_list, second_list))
