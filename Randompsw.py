# Random password generation code
import random
import string

length = int(input("Enter password length: "))

raw = string.ascii_letters + string.digits + string.punctuation

password = ""

for each in range(length):
    password += random.choice(raw)

print("Generated Password:", password)