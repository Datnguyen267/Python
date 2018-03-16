"""
- The Goal: Count birthday month
- Author: Dat Nguyen
- Create date: 2018-03-14
"""

from collections import Counter
import json

birthday_dict = {}
with open("info.json", "r", encoding='utf-8') as file:
  birthday_dict = json.load(file)

 
print("Welcome to the birthday dictionary. We know the birthdays of: ")
birthday_list = []
for person in birthday_dict:
  print(person)
  month = "".join(i for i in birthday_dict[person] if (not i.isdigit()) and (i != " "))
  birthday_list.append(month)

print(Counter(birthday_list))


