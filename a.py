try:
    file = open("abc.txt","r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File path is incorrect")
