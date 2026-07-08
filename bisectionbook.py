def f(x):
    return x**2-5*x+1


def initguess():
    for i in range(-2,2):
        if f(i) * f(i+1) <= 0:

             return i,i+1

# print("a,b = ",initguess())
a,b=initguess()

def bisection(a,b,tol):
     if f(a)*f(b)>=0:
          print("Invalid Interval!")
          return
     
     while(b-a)/2>tol:
          c=(a+b)/2

          if f(c)==0:
               return c
          
          elif f(a)*f(c)<0:
               b=c

          else:
               a=c

     return (a+b)/2

def main():
    # a=float(input("Enter lower limit (a): "))
    # b=float(input("Enter upper limit (b): "))
    tol=float(input("Enter tolerance: "))

    root=bisection(a,b,tol)

    if(root is not None):
        print("Approximate root=",root)

if __name__=="__main__":
        main()