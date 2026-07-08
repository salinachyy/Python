def f(x):
    return x**2-5*x+1

def initguess():
    for i in range(-2,2):
        if f(i) * f(i+1) <= 0:

             return i,i+1

print("a,b = ",initguess())