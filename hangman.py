"""
- The Goal: Try to guess a word in limit times.
- Author: Dat Nguyen
- Create date: 2018-02-09
"""

import random
def hangman():
  print("Let's play")
  list_number = {
    0: "Grateful",
    1: "Smile",
    2: "Happy",
    3: "Confident",
    4: "Honest",
    5: "Optimistic",
    6: "Care",
    7: "Generous",
    8: "Hope",
    9: "Charity"
  }

  while True:
    temp_key = random.randint(0, len(list_number))
    secret_word_origin = list_number[temp_key]
    del list_number[temp_key]
    secret_word = make_word_secret(secret_word_origin)
    print(secret_word)
    while secret_word.lower() != secret_word_origin.lower():
      user_guess = input("Please guess a character: ")
      secret_word = guess_word(secret_word, secret_word_origin, user_guess)
      print("The secret word is: " + secret_word)
    else:
      print("Great! You got it! The secret word is: " + secret_word_origin)
      
    if len(list_number) == 0:
      print("Thank you. See you again.")
      break
    else:
      user_input = input("Do you want continue?(Y/N)")
      if user_input.lower() != "y":
        break

"""
This function replace some characters in word into *.
params: word string
result: string with some *
"""
def make_word_secret(word):
  result = list(word);
  num_hidden_char = len(word) - 2
  while num_hidden_char > 0:
    temp_char = random.randint(0, len(word) - 1)
    if result[temp_char] != "*":  
       result[temp_char] = "*"
       num_hidden_char -= 1
  return "".join(result)

"""
This function compare guess character with word
params: word string
        word_origin string
        guess string
result: string
"""
def guess_word(word, word_origin, guess):
  result = list(word)
  word_origin = list(word_origin)
  count = 0
  for index, item in enumerate(word_origin):
    if item.lower() == guess.lower():
      count +=1
      result[index] = item
  print("There's %s character(s) %s in this word." %(str(count), guess))
  return "".join(result)


hangman()
