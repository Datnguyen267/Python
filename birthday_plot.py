"""
- The Goal: Birthday plot
- Author: Dat Nguyen
- Create date: 2018-03-14
"""

from bokeh.plotting import figure, show, output_file
from collections import Counter
import json

dict_map = {
  "01" : "January",
  "02" : "February",
  "03" : "March",
  "04" : "April",
  "05" : "May",
  "06" : "June",
  "07" : "July",
  "08" : "August",
  "09" : "September",
  "10" : "October",
  "11" : "November",
  "12" : "December"
        }

birthday_dict = {}
with open("scientist_birthdays.json", "r", encoding='utf-8') as file:
  birthday_dict = json.load(file)

 
print("Welcome to the birthday dictionary. We know the birthdays of: ")
birthday_list = []
for person in birthday_dict:
  print(person)
  birthday_list.append(birthday_dict[person][0:2])

birthday_list_char = []
for num in birthday_list:
  for char in dict_map:
    if num == char:
      birthday_list_char.append(dict_map[char])

count = Counter(birthday_list_char)
output_file("plot.html")

plot_x = [x for x in count]
plot_y = [count[x] for x in count]

plot = figure(x_range=plot_x)
plot.vbar(x=plot_x, top=plot_y, width=0.5)

show(plot)