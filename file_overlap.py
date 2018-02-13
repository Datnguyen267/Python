"""
- The Goal: Find overlap elemnents in two files
- Author: Dat Nguyen
- Create date: 2018-02-13
"""


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

prime = []
with open("primenumbers.txt", 'r') as open_file:
  line = open_file.readline()
  while line:
    prime.append(line)
    line = open_file.readline().splitlines()
    
happy = []
with open("happynumbers.txt", 'r') as open_file:
  line = open_file.readline()
  while line:
    happy.append(line)
    line = open_file.readline().splitlines()

print("Prime list: \n")
print(prime)
print("Happy list: \n")
print(happy)
print("Common list: ")
print(get_all_common_elements(prime, happy))
