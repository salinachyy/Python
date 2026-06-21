def greet():
    print ("Hello World")
greet()

def add(a,b=5): #default value of b .default value is always given to last parameter
    return a+b
# print(add(3))
print(add(2,3))