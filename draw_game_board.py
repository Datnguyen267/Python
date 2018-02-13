"""
- The Goal: Draw a game Board
- Author: Dat Nguyen
- Create date: 2018-02-13
"""

def draw(size):
  result = ''
  for i in range((int(size) * 2) + 1):
    if i % 2 == 0:
      for j in range(int(size)):
        result += ' ---'
    else:
      for j in range(int(size) + 1):
        result += '|   '
    result += '\n'
  return result

size = input("What size do do want? ")
print(draw(size))
