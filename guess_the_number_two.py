"""
- The Goal: Computer will guess a number a chosen. I will respone it's number is exact, high or low.
- Author: Dat Nguyen
- Create date: 2018-02-13
"""

def guess_the_number(min_range = 0, max_range = 100):  
  return int((max_range + min_range) / 2)

print("Let's play")
count = 0
min_range = 0
max_range = 100
while True:
  guess = guess_the_number(min_range, max_range)
  count += 1
  user_response = input("%s is secret number?(Y/N)" %(guess))
  if user_response.upper() != "Y":
    user_low_high = input("So, %s low or high?(L/H)" %(guess))
    if user_low_high.upper() == "H":
      max_range = guess
    elif user_low_high.upper() == "L":
      min_range = guess
    continue
  else:
    print("Yes, I known it is %s" % (guess))
    print("I guess %s time to get your number." % (count))
  ask_for_cont = input("Do you want to continue?(Y/N) ")
  if ask_for_cont.upper() != "Y":
    break
