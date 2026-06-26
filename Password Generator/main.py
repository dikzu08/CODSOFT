import random 
import string

pass_len = int(input("Enter Password Length : "))
charVal = string.ascii_letters + string.digits + string.punctuation
"""
password = ""
for i in range(pass_len):
   password += (random.choice(charVal))

print("Your random password is: ", password)

"""

result = "".join([(random.choice(charVal)) for i in range(pass_len)])
print("Your random password is: ", result)