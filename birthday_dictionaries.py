"""
- The Goal: Birthday dictionaries
- Author: Dat Nguyen
- Create date: 2018-03-13
"""

birthday_dict = {
    "Cristiano Ronaldo" : "5 February 1985",
    "Lionel Messi" : "24 June 1987",
    "Paul Pogba" : "15 March 1993"
  }

 
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for person in birthday_dict:
  print(person)
look_up = input("Who's birthday do you want to look up? ")
print(look_up + "'s birthday is " + str(birthday_dict[look_up]))
