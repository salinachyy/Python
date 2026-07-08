# Random password generation code
import random
import string

length = int(input("Enter password length: "))

raw = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(raw) for _ in range(length))

print("Generated Password:", password)