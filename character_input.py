"""
- The Goal: Ask and print user info
- Author: Dat Nguyen
- Create date: 2018-02-09
"""


def character_input():
  name = input("What's your name, sir? ")
  age = int(input("And how old are you? "))
  year_to_100 = 100 - age
  message = "Hello %s, you'll turn 100 in %s years." %(name, year_to_100)
  print(message)
  times = int(input("How many times do you want to print previous message? "))
  print("Now, it will print previous message %s times." % (times))
  for i in range(times):
    print(message)

character_input()
