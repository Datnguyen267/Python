"""
- The Goal: Read from file
- Author: Dat Nguyen
- Create date: 2018-02-13
"""

with open("nameslist.txt", 'r') as open_file:
  line = open_file.readline()
  while line:
    print(line)
    line = open_file.readline()
