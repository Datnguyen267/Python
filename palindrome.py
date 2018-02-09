"""
- The Goal: Check a string is a palindrome
- Author: Dat Nguyen
- Create date: 2018-02-09
"""

import random
def is_palindrome(string):
  result = False
  temp_list = list(string)

  if len(string) % 2 == 0:
    left_string = temp_list[0 : int(len(temp_list) / 2) : 1]
    right_string = temp_list[int(len(temp_list) / 2): len(temp_list) : 1]
    right_string = right_string[::-1]
  else:
    left_string = temp_list[0 : int(len(temp_list) / 2): 1]
    right_string = temp_list[(int(len(temp_list) / 2)) + 1 : len(temp_list) : 1]
    right_string = right_string[::-1]

  if left_string == right_string:
    result = True
  return result


string = input("Enter a string: ")
print(is_palindrome(string))
