import random

secret_number = random.randint(1, 100)

while True:
    choice1 = int(input("Guess a number: "))

    if choice1 == secret_number:
        print("WOW!!! You guessed it correctly")
        break
    elif choice1 > secret_number:
        print("Too high!")
    else:
        print("Too low!")