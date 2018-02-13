"""
- The Goal: Reverse word order
- Author: Dat Nguyen
- Create date: 2018-02-12
"""

import random
def reverse_word_order(string):
  result = string.split(" ")
  result = list(reversed(result))
  return " ".join(result)

sentence = input("Enter a sentence: ")
print(reverse_word_order(sentence))
