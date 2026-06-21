import random
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
for i in range(5):
    print(random.choice(string.ascii_letters))