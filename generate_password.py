"""
- The Goal: Generate password
- Author: Dat Nguyen
- Create date: 2018-02-12
"""

import random, string

def generate_password(choice):
  result = ""
  if choice.upper() == "W":
    result = weak_passwords[random.randint(0, len(weak_passwords))]
  else:
    result = random.sample(strong_passwords, 8)
    result = "".join(result)
  return result

weak_passwords = ['password', '123456']

strong_passwords = string.digits + string.ascii_letters + "!@#$%^&*()"

choice = input("Do you want weak or strong password(W/S): ")
print(generate_password(choice))
