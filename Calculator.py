num1=int(input("Enter first  number : "))
num2=int(input("Enter second number : "))
operator=input("Enter operator +,-,*,/,% : ")
def calculatevalue(num1,num2):
    if(operator=="+"):
        return num1+num2
    if(operator=="-"):
        return num1-num2
    if(operator=="*"):
        return num1*num2
    if(operator=="/"):
        return num1/num2
    if(operator=="%"):
        return num1%num2
print("Result : ",calculatevalue(num1,num2))
    

