import random
import string

def get_length():
    length = int(input("Enter the length of your password: "))
    return length


def generate_pswd():
    raw = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for _ in range(get_length()):
        password += random.choice(raw)
    return password

def display_pswd():
    print("Your password is: ", generate_pswd())

display_pswd()