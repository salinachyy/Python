str ="hello"
print(str[0])

str1=[1,2,3,4,5,'salina'] #List
print(str1[-1])
print(str1[1:5])   #slicing include 1 and exclude 5
del str1[1] #deletion in python



print('salina' in str1) #this checks salina inside the list if it is there result is true
print(1 not in str1)     #This checks:Is 1 NOT in the list?

str2=[1,2,3,4,5]
str2[0:4]=[10,20,30,40]  # include 0 and exclude 4, replace str2 with 10,20,30 this value
print(str2)


a=[1,2,3,8,9]
print("max = ", max(a))
print("Length of a = ",len(a))
print("Sum of numbers = ",sum(a))
print("minimum value = ",min(a))

b=[1,2,3,4,5]
for each in reversed(b): # it reads in backward direction
    print(each)

b=["java",'C',"DBMS"]
print(max(b))     #finds the “largest” string based on alphabetical



    

