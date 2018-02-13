"""
- The Goal: Show Fibonacci
- Author: Dat Nguyen
- Create date: 2018-02-12
"""

def fibonacci(number):
  result = []

  for i in range(int(number)):
    if i < 2:
      result.append(1)
    else:
      result.append(result[i-1] + result[i-2])
  return " ".join(str(x) for x in result)

number = input("Enter number: ")
print("%s numbers Fibonacci" %(number))
print(fibonacci(number))
