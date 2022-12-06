# Functions in Python
    #built in function and user define function

#built in function  sum()
from unittest import result

a = 5
b = 3
c = sum((a, b))
print(c)
# USer define function

def first_function():
    print(" This is first function in python :") 

# writing a function to calculate sum of two numbers 
def functSum( x, y):
    """This function calculate sum of two numbers"""
    z = x+y
    return z

print(first_function())  #return none because return statement is not set

a= int(input("Enter first number : "))
b= int(input("Enter second number : "))
sum_result = functSum(a, b)  #calling the sum function
print("Sum of ",a,"And",b," is =",sum_result)

#doc string is written in the first line of any function which describes about what the function do
# printing the doc string 
print(functSum.__doc__)


