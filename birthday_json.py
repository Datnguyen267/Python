"""
- The Goal: Get birthday dictionaries in json
- Author: Dat Nguyen
- Create date: 2018-03-14
"""

import json

birthday_dict = {}
with open("info.json", "r", encoding='utf-8') as file:
  birthday_dict = json.load(file)

def set_dict():
  data = {}
  name = input("Who's birthday do you want to append? ")
  date = input("When is {} born?".format(name))
  print("OK, " + name + "'s info is going to append.")
  birthday_dict[name] = date
  
  with open("info.json", "w") as file:
    json.dump(birthday_dict, file)


def get_dict():
  with open("info.json", "r", encoding='utf-8') as file:
    birthday_dict = json.load(file)
  look_up = input("Who's birthday do you want to look up? ")
  if birthday_dict[look_up]:
    print("{}'s birthday is {}.".format(look_up, str(birthday_dict[look_up])))
  else:
    print("There's no have " + look_up)

 
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for person in birthday_dict:
  print(person)
  
choose = input("Do you want SET or GET? ")
if choose == "SET":
  set_dict()
elif choose == "GET":
  get_dict()
else:
  print("Your input neither SET nor GET. So, I quit.")


