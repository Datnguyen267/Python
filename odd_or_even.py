"""
- The Goal: Check a number is odd or even
- Author: Dat Nguyen
- Create date: 2018-02-09
"""


def odd_or_even(number):
  result = ''
  if number %2 == 0:
    result = "even"
    if number % 4 == 0:
      result = "divided evenly by 4"
  else:
    result = "odd"

  return "The number %s is %s." %(number, result)

def check_two_numbers_even(first, second):
  result = ""
  if first % second == 0:
    result = "evenly"
  else:
    result = "not evenly"
  return "%s divides %s into %s." %(first, result, second)

number = int(input("Enter a number: "))
print(odd_or_even(number))

first_number = int(input("Enter first number: "))
second_number = int(input("Enter sencond number: "))
print(check_two_numbers_even(first_number, second_number))
