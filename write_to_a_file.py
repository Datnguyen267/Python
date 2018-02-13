"""
- The Goal: Write to a file
- Author: Dat Nguyen
- Create date: 2018-02-13
"""


file_name = input("Enter file name: ")
with open(file_name + ".txt", 'w') as open_file:
  open_file.write("Practice Python more!")
